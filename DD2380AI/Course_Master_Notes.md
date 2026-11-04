# DD2380 Artificial Intelligence — Course Master Notes (HT26)

> **What this is:** a standalone master study guide compiled from *all* lecture slides and assigned literature currently in the course folder (Lectures 1a, 1b and the AI Ethics & Society lecture of 29 Oct 2026, plus its three assigned readings and two templates). It is written for a student with zero prior knowledge: every piece of jargon is defined before it is used, quiz-grade facts are bulleted, and each module ends with lab-presentation preparation. Future lectures can be appended seamlessly using the module template at the bottom. **Part II** (after the lecture modules, before the appendices) is a separate quiz-targeted revision layer built from the HT25 Canvas quizzes in `LastQuizzes/` — start there in the 48 h before any quiz.

---

## Course at a Glance — The Assessment Map

**You must pass every component.** The final grade comes from the labs alone, but only if everything else passes.

| Component | Format | Passing rule | Key dates (all deadlines 19:00) |
|---|---|---|---|
| **RAP1 Essay** | Individual reflection (500–600 words) → group discussion (3–4 people, 4 preferred) → group summary (500–600 words) on risks & benefits of AI | Pass/Fail | Opens 29 Oct · **Due Mon 9 Nov** |
| **TENQ — On-campus quizzes (3)** | 8 multiple-choice questions, 45 min, one per main topic (Search, HMMs, RL) | Pass/Fail, **≥50% (4/8)**; max one regular-period retake; re-exam period: one retake each | Slots signed up via Canvas → Calendar → Appointments |
| **TENQ — Canvas quizzes (6)** | Online, released after each topic lecture; individual, 60 min, 5 attempts | Pass/Fail, typically 4–5/6 points | Before each quiz deadline |
| **LAB2 — 3 programming assignments** | **Search**, **HMMs**, **RL**; each structured in levels **E–D, C, B–A**; pairs strongly encouraged; Python required | Graded A–F; Kattis gives the *grade range*, the Learning Journal gives the *grade within range*, the oral exam gives the *individual cap* | Search opens 3 Nov, **due 23 Nov**; HMM opens 13 Nov, **due 30 Nov**; RL opens 23 Nov, **due 7 Dec** |
| **Oral exams** | Random topic (Search, HMM or RL) per student; you must explain your code + journal | Sets your individual max LAB2 grade | 8 & 11 Dec, 15–17 Dec, 4 Jan |
| **Final quiz slots** | Any topic | — | 4–5 Jan |

- **Final grade = LAB2 grade** = rounded-down average of Search, HMM, RL — *capped* by (a) your individual oral exam and (b) the deadline rule: **grade A requires all code + journals on time; any late submission ⇒ max B**.
- **Prerequisite for LAB2:** the Code-of-Conduct quiz on Canvas.
- **Kattis:** register at `https://kth.kattis.com/courses/DD2380/ht26` (log in first).
- **Textbook:** Russell & Norvig, *Artificial Intelligence: A Modern Approach* (Pearson New International Edition, 2013).
- **Communication:** Canvas discussion forums first; email only for private/personal matters → `rpl-ai-teachers@eecs.kth.se`; English only. Announcements = important & urgent.
- **Course crew:** André Pereira (course responsible, Problem Solving, Taming Uncertainty), Iolanda Leite (Ethics), Petter Ögren (RL, Multi-Agent Systems + Robotics), Noemie Jaquier (Logic & Planning); guest lecturers Josephine Sullivan, Johan Boye, Gabriel Skantze, Mårten Björkman, Gustav Eje Henter; ~10 TAs (weekly 1-1 Zoom "office hours" via the KTH queue, mostly Tuesdays).

---

## Lecture 1a: Introduction to AI

### TL;DR

This lecture answers **"what is AI?"** and installs the vocabulary you will use for the entire course. It walks through AI's history (from the 1956 Dartmouth Conference through AI winters to the 2022 ChatGPT boom), places today's hype on Gartner's Hype Cycle, and then settles on the course's working definition of AI: the **rational-agent approach** from Russell & Norvig — an agent that does *the right thing given what it perceives*, i.e., chooses the action expected to maximize its performance measure. Perfect rationality is impossible in practice (computational limits, imperfect information), so real AI is about *approximate/bounded* rationality.

The practical takeaway is the **PEAS framework** and the **environment-property taxonomy**: before you build anything (including your Search/HMM/RL labs), you must be able to specify Performance measure, Environment, Actuators, Sensors, and classify the environment (fully/partially observable, deterministic/stochastic, episodic/sequential, static/dynamic, discrete/continuous, single/multi-agent, cooperative/competitive). Those classifications determine *which AI technique applies* — e.g., stochastic + sequential + partially observable problems are exactly what HMMs and MDPs/RL were invented for.

### Quiz Flash-Facts & Vocabulary

**Core definitions (know these cold):**
- **AI (four viewpoints, Russell & Norvig):** ① Thinking humanly ② Acting humanly (Turing Test) ③ Thinking rationally (logic) ④ **Acting rationally (the rational-agent approach — the one this course primarily adopts).**
- **Agent:** anything that **perceives** its environment through **sensors** and **acts** upon it through **actuators**.
- **Agent function:** the mathematical mapping from percept history to action.
- **Rational behavior:** choosing the action *expected* to maximize the performance measure, **given the available information** (percepts + built-in knowledge).
- **Perfect rationality is impossible** in practice because of computational limits and imperfect information → real systems are rationally *bounded*.
- **PEAS:** Performance measure, Environment, Actuators, Sensors — the 4-part spec of any agent task.
- **Performance measure:** the criterion for "success" (not the same as the agent's behavior).

**History timeline (favorite multiple-choice fodder):**

| Year | Event |
|---|---|
| 1956 | **Dartmouth Conference** — the term "Artificial Intelligence" is born |
| 1959 | Computers play checkers better than the average human |
| 1974–80 | Funding cuts — the first **"AI winter"** |
| 1985 | ~1 billion dollars spent on expert systems |
| 1987 | Market for specialized AI hardware collapses |
| 1997 | IBM **Deep Blue** beats Garry Kasparov (chess) |
| 2012 | **Deep learning** breakthrough on **ImageNet** |
| 2016 | **AlphaGo** beats Lee Sedol (Go) |
| 2017 | **"Attention Is All You Need"** — Transformers |
| 2022 | **ChatGPT** |

**Gartner's Hype Cycle — the five stages in order:** 1) Innovation Trigger → 2) Peak of Inflated Expectations → 3) Trough of Disillusionment → 4) Slope of Enlightenment → 5) Plateau of Productivity. (Quiz risk: ordering and names, especially stages 2–4.)

**Numbers:**
- Global web searches for "AI" almost **quadrupled, 7.9M → 30.4M**, between June 2022 and March 2023.
- ChatGPT users: ~**100M in Nov 2023 → >1,000M by Aug 2026**.
- Harvard undergraduate study (Aug 2024, n=326): **87.5%** use generative AI at least weekly; ChatGPT by far the most popular; used to answer questions, replace Wikipedia-style lookups, and support writing/programming.

**AI capability areas (how AI problems group):** solve problems (search, adversarial search) · reason/plan/decide (logic, inference, planning, reinforcement learning) · learn (machine learning, neural nets) · communicate & perceive (vision, speech, NLP) · move & manipulate (robotics).

### Core Methodologies / Theories → Lab Relevance

**1) The PEAS specification.** For any new problem, write down the four cells before coding:

| | **Assembly robot arm (worked example)** | **Chess engine (practice)** | **Autonomous car (practice)** |
|---|---|---|---|
| **Performance measure** | % correctly assembled, speed, damage/safety, energy/cost | Win rate / rating | Safe arrival, legality, comfort, time |
| **Environment** | Conveyor belt with pieces | Board + opponent | Roads, traffic, pedestrians |
| **Actuators** | Arm motors, gripper | (Virtual) move output | Steering, throttle, brake |
| **Sensors** | Cameras, joint positions, force-torque | Board state | Cameras, lidar, GPS, IMU |

**2) Environment properties (the lab-critical taxonomy):**

| Property | Question it answers |
|---|---|
| Fully vs **partially** observable | Does the agent see *all* relevant state? (HMMs exist because real problems are partially observable) |
| Deterministic vs **stochastic** | Does an action uniquely determine the next state? (stochastic → probability needed: HMMs, MDPs) |
| Episodic vs **sequential** | Do earlier actions affect later decisions? (sequential → planning, RL) |
| Static vs **dynamic** | Can the world change while the agent deliberates? (dynamic → time pressure, online search) |
| Discrete vs **continuous** | Are states/actions/time discrete? (continuous → discretization or continuous methods) |
| Single vs **multi-agent** | Do other agents' actions matter? (multi-agent → game theory / adversarial search) |
| Cooperative vs **competitive** | Aligned or opposed objectives? (competitive → minimax, alpha-beta) |

The assembly robot arm's environment is: **partially observable, stochastic, sequential, dynamic, continuous, single-agent** — a sentence you should be able to produce and *justify* in a presentation.

**3) How this maps onto your labs:** Search labs mostly assume fully observable, deterministic, single-agent worlds (informed/uninformed search); the Games lecture introduces *competitive multi-agent* environments; HMM labs model *partially observable, stochastic, sequential* processes; RL labs assume *stochastic, sequential, dynamic* (MDP) worlds where the agent learns from rewards. Stating these classifications at the start of any lab presentation immediately shows mastery.

### Literature Synthesis

- **Russell & Norvig (AIMA, 2013)** is the recommended textbook and the source of the rational-agent framing. Its key argument for you to internalize: the *acting rationally* view subsumes the others (a rational agent can pass a Turing test or prove theorems if doing so maximizes its performance measure) and is the most general, testable design stance. The agent function's intractability motivates the course's trade-off discussions (heuristics, approximations, learned policies).

### Lab Presentation Prep

1. **Open every lab talk with a PEAS + environment-properties slide** for your assignment problem. It costs 30 seconds, frames everything, and pre-empts the most common examiner question ("why did you pick algorithm X?" — answer: *because the environment is {observable? deterministic? competitive?}*).
2. **Justify algorithm choice from environment properties**, e.g., "the problem is partially observable and stochastic, so a plain deterministic planner is unsound — hence HMM filtering/RL."
3. **Name the performance measure you optimized** and distinguish it from intermediate heuristics (e.g., A*: path cost vs heuristic estimate) — examiners probe exactly this distinction.
4. **Anticipate the limitations slide:** bounded rationality means your agent can't be perfectly rational; state what you approximated and why (time/memory).
5. **Tie results to the timeline/hype vocabulary:** e.g., "unlike the 1985 expert-systems hype, our approach is evaluated on measurable performance criteria" — shows you connect lecture theory to practice.

---

## Lecture 1b: Course Practicalities

### TL;DR

This lecture defines **how you are examined** and, more importantly, *how to think about* the examination structure. The course has three gates: an **essay** (ethics, pass/fail), **quizzes** (3 on-campus + 6 on Canvas, all pass/fail, designed to force continuous learning), and **three programming labs** (Search, HMMs, RL) that are graded A–F and form the entire final grade. Kattis tests give you a grade *range*; your written Learning Journal determines the grade *within* that range; an individual oral exam then caps it, and any late submission caps the whole LAB2 grade at B.

The second thesis is *logistics discipline*: the lecture spends half its time on where things live (Canvas modules, Kattis, appointments for tutorials/quizzes/oral exams) and how to communicate (Canvas forums first, `rpl-ai-teachers@eecs.kth.se` only for private matters, English only). The practical tips from previous generations — **do Canvas quizzes right after each lecture, start programming assignments the day they open** — are effectively exam strategy, not fluff.

### Quiz Flash-Facts & Vocabulary

- **Intended Learning Outcomes (ILOs):** ① apply different AI principles ② choose appropriate tools and implement efficient solutions ③ integrate tools into programs with "intelligent" properties ④ present, analyze and defend an own AI solution ⑤ reflect on social & ethical aspects of AI — so that you can (a) use AI methods in analysis/design/implementation and (b) contribute to intelligent-system design in academia *and* industry.
- **Lecture map:** Intro/Practicalities → AI & society → Problem solving (Search, Games) → Logic & planning → Taming uncertainty (probabilistic reasoning, Bayesian networks; HMMs) → Decision making under uncertainty (MDPs/POMDPs; RL) → Multi-agent systems + robotics → Machine learning → NLP & conversational systems → Computer vision → Generative AI & wrap-up.
- **Grading table:** Essay Pass/Fail · Quizzes Pass/Fail · Search/HMM/RL each A–F. **Final grade = LAB2 grade** (rounded-down average of the three labs), subject to the oral-exam cap and the deadline cap.
- **Kattis does NOT give the grade** — it gives the highest grade range you are eligible for; **the journal decides the grade within that range**.
- **On-campus quiz format:** 8 multiple-choice questions, 45 minutes, pass at 50% (4/8); during the regular period you may repeat **one** (possible slots 4–5 Jan); in the re-exam period each can be repeated once.
- **Canvas quiz format:** released after each topic lecture; typically **4–5/6 points to pass**; individually, 60 min, **5 attempts**, before the deadline; multiple-choice/multiple-answer.
- **Programming assignments:** each has **E–D, C, B–A levels**; pairs strongly encouraged; assessed by **Kattis (correctness)** + **Assignment Learning Journal (solution, design choices, limitations, reflection questions)**.
- **Oral exam:** each student is examined on **one randomly selected** of Search/HMM/RL; must explain assignment, code, and journal; it **caps** your individual LAB2 grade.
- **Deadline rule:** all code + journals on time ⇒ eligible for A; **anything late ⇒ maximum final LAB2 grade B**.
- **Key deadlines:** Essay due **Mon 9 Nov 19:00** · Search due **Mon 23 Nov 19:00** · HMM due **Mon 30 Nov** · RL due **Mon 7 Dec** · Oral exams 8 & 11 Dec, 15–17 Dec, 4 Jan · Final quizzes 4–5 Jan.
- **Communication:** email `rpl-ai-teachers@eecs.kth.se` for things like "part of my group disappeared" / "I did part of the course in HT22" — NOT for "when is the tutorial?" (that goes to Canvas forums/announcements).
- **Registration TODOs:** register for the course (web) → Canvas (turn on Announcement, Conversation, Appointment notifications) → **Code-of-Conduct quiz now** → Kattis account + course registration → know your Python.

### Core Methodologies / Theories → Lab Relevance

**The three-tier grading pipeline (this is *the* model to explain at any oral exam):**
1. **Kattis (automated):** verifies correctness against hidden tests → yields the **highest grade range** you're eligible for (E–D / C / B–A). Passing more tests unlocks higher ranges; Kattis never *awards* the grade.
2. **Assignment Learning Journal:** your written explanation of the solution, **design choices, limitations, and reflection questions** → determines the **actual grade within** the Kattis range. This is where presentation-quality argumentation matters: an unexplained hack can cost you the range's top.
3. **Individual oral exam:** you must be able to **explain the assignment, your code, and your journal** for the one randomly chosen lab → sets your **individual maximum** LAB2 grade.
4. **Deadline rule:** everything on time ⇒ A possible; anything late ⇒ max B. (Plan around 19:00 Kattis/Canvas cutoffs.)

**Why the structure is designed this way (useful to say in presentations):** quizzes force *recall and application* of basic concepts continuously (spaced repetition); the labs force *hands-on implementation*; the journal + oral force *explicit reasoning about design choices* — exactly the skill the ILOs demand ("present, analyse, and defend an own solution").

### Literature Synthesis

- **Course literature = the Canvas modules + Russell & Norvig.** The schedule itself encodes the reading order: essay material (ethics) is consumed *now*, Search immediately after, etc. The practical reading strategy implied by the lecture: treat each lecture's Canvas quiz as the "reading check" for that module, and treat R&N chapters as reference (not cover-to-cover).

### Lab Presentation Prep

1. **In every journal, structure exactly three things:** (a) *what* the algorithm does, (b) *why* the design choice is sound for this problem's environment properties, (c) *limitations* + what you'd do with more time. The oral exam rubric tracks this structure.
2. **Anticipate the "Kattis question":** be ready to state which grade range you unlocked and argue why your journal deserves the top of it — cite the specific design trade-off you made.
3. **Prepare the "defense" angle for your code:** examiners will ask why a function looks the way it does; write the journal as a future-you defense document.
4. **Deadline risk framing:** if something is late, the whole LAB2 caps at B — mention in presentations that timeliness was a *deliberate* engineering constraint (MVP first, polish second).
5. **Use the essay as presentation practice:** the ethics module's presentation prep below doubles as your first graded oral/written defense of technical choices.

---

## Lecture 2: Introduction to (Practical) AI Ethics

> *Given by Iolanda Leite, 29 Oct 2026 (original slides by Katie Winkle). Sources: lecture `Intro_AIEthics_Oct29.pdf`, Šabanović 2010, Winfield & Winkle 2020 (RoboTed), the BS 8611 hazard table PDF, and the Ethics Canvas template.*

### TL;DR

This lecture reframes "ethics" from a philosophical abstraction into an **engineering practice**. Part 1 surveys *topical* AI ethics problems — energy & exploitation (training a big model can cost ~50 kW per hour vs ~1 W for a human brain), anthropomorphism & deception (Hello Barbie, Embodied's Moxie shutdown, Google Duplex), and sexism/racism (UNESCO's gendering of assistants, Buolamwini & Gebru's *Gender Shades* showing up to 34.7% error on darker-skinned women vs 0.8% on lighter-skinned men). The lecture's working definition of **Ethical AI = any and all AI designed, developed and deployed ethically**, with **"do no harm"** as the minimum principle — and the claim that doing this makes *better* (smarter, more impactful, more innovative) technology, not a constrained one.

Part 2 gives you the two **practical tools** the course will actually grade you on: **(1) a mutual-shaping approach** to technology and society (replacing the flawed *technological determinism* view), and **(2) ethical standards & risk assessment** (BS 8611's hazard taxonomy, IEEE's Ethically Aligned Design, the EU AI Act, ISO 42001), culminating in the worked examples of **RoboTed** (ERA of a smart teddy bear) and the **Autonomous Robot Fitness Coach** (mutual-shaping pipeline + ERA tasks). The essay assignment *is* the assessment of this lecture: read ≥2 papers, reflect individually, discuss in a group, write a group summary.

### Quiz Flash-Facts & Vocabulary — Part A (Topical Issues)

**Definitions first (zero-knowledge baseline):**
- **Ethics (in this course):** the practical study of the ethical implications of AI and of *how to develop new technologies ethically* — grounded in empirical research, not abstract philosophy.
- **Anthropomorphism:** attributing human traits (feelings, intentions) to non-human agents. **Deception (in HRI):** a user wrongly believing a machine has capacities/feelings it doesn't (e.g., "the robot cares about me").
- **Bias (statistical/systemic):** systematic error in an AI's behavior caused by unrepresentative training data or design assumptions — e.g., facial analysis failing more on darker-skinned women.
- **Intersectional disparity:** an error pattern affecting the *combination* of identities (gender × skin tone), not either alone.

**Energy & exploitation (from Prof. Alan Winfield's "AI's dirty secrets"):**
- Training/compute comparison slide: **50 kW (≈ an industrial lighting generator, 50,000× a Sedol)** vs the human brain's **170 kcal ≈ 1 W (≈ an LED nightlight)**.
- Key paper: **Strubell, Ganesh & McCallum (2019), "Energy and Policy Considerations for Deep Learning in NLP"** (ACL 2019) — exposed the carbon & cost footprint of NLP model training.
- Newer example: **Luccioni, Jernite & Strubell (2024), "Power Hungry Processing: Watts Driving the Cost of AI Deployment?"** (ACM) — shifts attention from *training* to *deployment/inference* energy.
- Quiz angle: AI's footprint has **two hidden costs** — energy (carbon) and **exploited/underpaid labor** (data annotation, content moderation).

**Anthropomorphism & deception — case studies (memorize the one-line story):**
- **Hello Barbie (2015):** WiFi-connected talking doll; hackers could hijack it to spy on children → discontinued (CNBC: "say goodbye to Hello Barbie").
- **Embodied Inc.'s Moxie** (social robot for childhood development): company **shut down Dec 2024**; parents documented children *grieving a "dying" companion*; now catalogued as an **OECD AI incident**.
- **Google Duplex** (2018): assistant that calls humans and inserts "umms/ahs" — criticized because the human didn't know they were talking to a machine (deception-by-design).
- **UNESCO report "I'd Blush if I Could"** (2019): female-gendered assistants (Siri, Alexa) are designed as **obliging, docile, eager-to-please**; they tolerate sexual harassment/insults and sometimes flirt back → propagates harmful gender stereotypes.
- **Robot backchannel-bias case study (Parreira, Gillet, Winkle & Leite, HRI 2023):** robot's listening behavior was trained on corpora with skewed gender distributions (e.g., 0F/6M speakers) → robot behaved *differently across user identities*. Lesson: **quantify behavior before deployment**; don't rely on perception studies alone; decide *how the robot should behave*: ① reproduce human-human differences, ② treat all identities equally, ③ overcompensate.

**Sexism, racism & (mis)representation:**
- **Buolamwini (Data Feminism / Gender Shades):** the face dataset behind widely-used facial analysis contained **78% male, 84% white** faces — her own face wasn't recognized in a class project.
- **Buolamwini & Gebru, "Gender Shades" (FAccT 2018):** on commercial gender classification, **darker-skinned females are the most misclassified group with error rates up to 34.7%; maximum error for lighter-skinned males: 0.8%**.
- **Twitter image-cropping scandal (2020):** the saliency crop algorithm favored white faces → Twitter apologized; shows biases can emerge from *seemingly neutral* engineering choices.
- **AI-generated fakes in politics:** fabricated images of politicians/celebrities (e.g., AI-generated "endorsements") as election disinformation (2024 US election reporting).
- **Copyright & creativity:** "AI hallucinations" of authors (Naomi Klein's case) and DALL·E-style generation raise fair-use/copyright questions.
- **Broader framing:** *Tech + Social (In)Justice* — Ben Shneiderman's Human-Centred AI; AI4SG (AI for Social Good) movement; at KTH: AI + UN Sustainable Development Goals, feminist social robots, inclusion of newly arrived children.

**The lecture's three-layer definition of "Ethical AI" (venn-style, know all three):**
1. **Designing & developing (any and all) AI ethically** — responsible innovation in design/deployment; critical evaluation of real-world impact; **"Do No Harm" as the minimum principle**.
2. **Moral decision-making in/with/by AI** — e.g., the trolley problem.
3. **Actively tackling social injustice with AI** — AI4SG, unbiased recruitment, AI + SDGs, feminist social robots, inclusion projects.

### Quiz Flash-Facts & Vocabulary — Part B (Standards, ERA, Regulation)

**Mutual shaping vocabulary:**
- **Technological determinism (TD):** the belief that technology drives history/society — "**Science finds → industry applies → man conforms**". Signs: technological advancement ≡ societal success; focus on *justifying technological fixes* rather than understanding the problem; design choices made only by "technical" experts. TD neglects human agency and ignores social context.
- **Technological fix:** applying technology to solve a social problem that is non-technical in nature.
- **Mutual shaping / co-production:** technology and society shape each other bidirectionally; design involves social *and* technical choices; it is an approach to developing tech, not just a theory.
- **Socio-technical ecology:** the full system of people, practices, spaces and technologies around a technology's use.
- **Stakeholders:** people directly impacted by the technology who hold *tacit knowledge* of the application domain.
- **Participatory design / co-design:** involving users/domain experts in design: focus groups, interviews, workshops, interdisciplinary hackathons, crowdsourcing.
- **Wicked problem:** a design problem with no linear progression from definition to solution, no exhaustive rules, multiple valid explanations — the designer bears full responsibility for outcomes (characterizes social robotics).

**Standards & regulation vocabulary:**
- **Principles vs Standards:** ~25 sets of ethical principles for robotics/AI existed by 2019 (earliest: Asimov 1950; 22 published from 2017 onwards). **"Principles are not practice."** Standards bridge good intentions → good practice (as in aviation, medicine).
- **Asimov's Three Laws of Robotics (1950):** ① A robot may not injure a human being or, through inaction, allow a human being to come to harm. ② A robot must obey orders given by humans except where they conflict with the First Law. ③ A robot must protect its own existence as long as this does not conflict with the First or Second Laws. (Importance: established that robots *should be governed by principles*.)
- **The trust chain:** **Ethics → Standards → Regulation ⇒ Trust.** Standards let us "create and utilise expert-informed standards to share best practices & ensure we are delivering safe, effective & verifiable systems."
- **BS 8611 (BSI):** "Robots and robotic devices. Guide to the ethical design and application of robots and robotic systems." **First explicitly ethical standard in robotics (2016; updated 2023).** *Not* a code of practice — guidance for performing an **ethical risk assessment**. Contains **20 distinct ethical hazards/risks in 4 categories: Societal, Application, Commercial/Financial, Environmental**, each with mitigation advice + verification/validation suggestions.
- **IEEE Ethically Aligned Design (EAD1e):** global initiative ("IEEE Ethics in Action") giving pragmatic recommendations for technologists/educators/policymakers; organized around **Three Pillars** connected to high-level **General Principles**; informing ~**14 standards** (many published, some in progress — working groups open to join). "Standards exist; the question is adoption…"
- **EU AI Act:** risk-based regulation of AI: **Unacceptable-risk** systems (social scoring, harmful manipulation) are **banned**; **High-risk** systems (healthcare, law enforcement…) are **strictly regulated**; **transparency requirements** for generative AI (e.g., ChatGPT). Expected to "begin" 2026, with delays (Omnibus agreement postponed high-risk deadlines).
- **EU Ethics Guidelines for Trustworthy AI:** *recommendations* (not law) — contrast with the AI Act which is **legally binding with enforcement mechanisms**. Both emphasize a **human-centric approach** prioritizing safety, well-being, fundamental rights.
- **ISO 42001:** AI governance & compliance management-system standard (the ISO equivalent of ISO 27001 for AI).

**ERA & tooling vocabulary (verbatim-grade definitions):**
- **ERA core definitions (BS 8611):** **ethical harm** = "anything likely to compromise psychological and/or societal and environmental well-being"; **ethical hazard** = "a potential source of ethical harm"; **ethical risk** = "probability of ethical harm occurring from the frequency and severity of exposure to a hazard".
- **Risk assessment's 3 stages (generic, from RoboTed):** ① identify & analyze potential events (**hazards**) that may cause harm to individuals/property/environment; ② judge acceptability & likely impact of harm from exposure (**risks**); ③ determine steps to **mitigate** risks to minimize/eliminate harms. (Safety precedents: **ISO 14971** medical devices, **ISO 12100** machinery safety.)
- **Responsible Robotics** (RoboTIPS definition): "the application of Responsible Innovation in the design, manufacture, operation, repair and end-of-life recycling of robots, that seeks the most benefit to society and the least harm to the environment." ERA should sit within a Responsible-Innovation framework such as EPSRC's **AREA** (Anticipate, Reflect, Engage, Act) plus ethically-aligned (IEEE) and values-based design.
- **Ethical black box:** a data logger on a robot so accidents can be investigated (analogue of an aircraft flight recorder); ERA is "the opposite face of robot accident investigation — seeking, at design time, to prevent risks becoming accidents."
- **Ethics Canvas** (ADAPT Centre / Trinity College Dublin, v1.8, 2017): an ethics workshop tool adapted from Osterwalder's **Business Model Canvas** (CC BY-SA 3.0). Nine boxes (numbered in workshop order): ① **Individuals affected** (men/women, user/non-user, age categories…) ② **Groups affected** (communities, unions, regulators…) ③ **Product or service failure** (tech/human error, security breach, data loss…) ④ **Problematic use of resources** (climate, privacy, employment impacts…) ⑤ **Worldviews** (how the project changes perceived roles in society) ⑥ **Group conflicts** (impact on relations between groups, e.g., employers vs unions) ⑦ **Relations** (problematic changes in individual behavior/habits) ⑧ **Behaviour** (individualistic/materialistic shifts, etc.) ⑨ **What can we do?** — pick the **four most important impacts** and redesign, add recommendations for use, or spell out the values driving the design.

**Worked-example numbers (quiz fodder):**
- NHS **Couch to 5K**: 27 sessions, 3×/week for 9 weeks; early sessions = short runs with walking (e.g., 1 min walk + 1.5 min run × 8); goal: ~30 min non-stop / 5 km; delivered via app; for all ages without major health concerns.
- **Expert-in-the-Loop IML study:** **>12 hours co-design sessions** with a domain expert; deployed **3 months in a university gym**; **10 participants (1 dropout)**; **232 exercise sessions total = 151 supervised (training the ML) + 32 autonomous (trained ML) + 49 autonomous (heuristic "control")**.
- RoboTed risks use likelihood levels **(H)igh / (M)edium / (L)ow**.

### Core Methodologies / Theories → Lab Relevance

**Methodology 1 — Taking a mutual-shaping approach (two practical moves):**

- **Move A: Situate technology design in society (Šabanović's first pillar).**
  - **[1A] Evaluate technology in society:** get out of the lab — test "in the wild", in target environments, with actual users.
  - **[1B] Study socio-technical ecologies:** systematic study of the context of use *before* designing/building, and *again after* deployment (performance, usage styles, impact on the ecology).
  - **[1C] Outside-in design:** combine 1A+1B into an iterative cycle — "starts with situated observation and empirical research and follows with an iterative process of prototype building and testing in the real world to construct robots through a continuing conversation with the social environment of their use." Constraints come from empirical social research, not technical capabilities; final evaluation uses users' subjective experience, not internal technical benchmarks.
- **Move B: Involve society in technology design (participatory design).**
  - Include **stakeholders** (directly impacted people with tacit domain knowledge) early — for "socially robust, rather than merely acceptable" technology.
  - Methods: focus groups, interviews, workshops, interdisciplinary hackathons, crowdsourcing.
  - **Expert-in-the-Loop Interactive Machine Learning as participatory design (3 steps):** ① co-design the robot's action & input space *with* a domain expert; ② co-design a "teaching interface" for using those actions & responding to robot suggestions; ③ the domain expert teaches the robot via IML *in-the-wild*. Documented wins: new application ideas + required data; real-world considerations crucial to acceptability; **significantly increased experts' own acceptance** of robots. Known gap in that study: **no design/development work with target users**.

**Methodology 2 — Ethical Risk Assessment (ERA): the RoboTed worked example.**

ERA = standard 3-stage risk assessment with the *envelope extended* from safety risks to ethical risks (BS 8611). The RoboTed case study (Winfield & Winkle, ICRES 2020) analyzes a hypothetical smart teddy bear — **technology:** WiFi-connected; cloud speech recognition + chatbot AI + local speech synthesis; camera eyes for (local) face recognition; motorized arms/legs for baby-like crawling. **Designed to:** recognize its owner (face + name, turns toward child); respond to hugs/tickles; tell stories (with interruptions/repeats); sing songs (encourage singing along); act as a **child minder** (parents remotely listen/watch/speak). The paper runs 4 risk tables, each: Hazard | Risk | Level (H/M/L) | Mitigation.

**Table 1 — Physical (safety) risks:**

| Hazard | Risk | Level | Mitigation |
|---|---|---|---|
| Tripping | Users trip over RoboTed crawling on the floor | M | Audible crawling sound to alert users |
| Battery overheating | Defective batteries/chargers overheat or catch fire | M | Use low-risk consumer rechargeable batteries (not Li-Ion); advise parents to supervise charging |

**Table 2 — Psychological risks:**

| Hazard | Risk | Level | Mitigation |
|---|---|---|---|
| Addiction | Child plays obsessively, neglects family | M | "RoboTed needs to sleep now" function |
| Deception (of child) | Child believes RoboTed has feelings for her | M | Chatbot avoids language suggesting feelings (no "I like you") |
| Over-trusting (by child) | Child can't distinguish autonomous vs child-minder mode → shares secrets parents hear (or vice versa) | **H** | Notification when child-minder mode activates; use parents' voice, not RoboTed's voice |
| Over-trusting (by parents) | Parents over-rely on child-minder function | **H** | **Remove the child-minder function entirely** |
| The Uncanny Valley | Child becomes fearful of near-but-not-quite lifelike robot | L | Cartoon voice; early user trials with children |

**Table 3 — Privacy & security risks:**

| Hazard | Risk | Level | Mitigation |
|---|---|---|---|
| Weak security | Hackers gain access to RoboTed's sensors & control functions | **H** | Strong encryption + best-practice password protection |
| Privacy | Personal data (images, voice recordings of child) stolen | M | Auditable measures ensuring data is deleted immediately after use |
| Lack of transparency | No data logs ⇒ accidents impossible to investigate | **H** | Build in a secure local data logger = **ethical black box** (last few hours only) |

**Table 4 — Environmental risks:**

| Hazard | Risk | Level | Mitigation |
|---|---|---|---|
| Unsustainability (materials) | Unsustainable or high-carbon materials | M | Sustainable fur sources; avoid plastics (e.g., wooden skeleton) |
| Unrepairability | Lifetime limited because faults can't be repaired | M | Design for repair: replaceable parts (esp. battery) + repair manual |
| Unrecyclability | End-of-life robots dumped in landfill | M | Design for recycling; remaining materials biodegradable |

**What ERA is proven to buy you (the paper's own conclusion — quote-worthy):** attention to ethical risks can ① **suggest new functions** ("RoboTed needs to sleep now"), ② **draw attention to design modifications**, ③ **highlight the need for user engagement**, and ④ **reject some functionality as too risky** (the child minder). **Known limitations of ERA (memorize for your essay):**
- ERA **cannot guarantee exposing all risks** — it is a *subjective* process; the team must think critically & creatively about "what could go wrong" — Vallor et al.: the "habit of exercising the skill of **moral imagination** to see how an ethical failure of the project might easily happen, and to understand the preventable causes so that they can be mitigated or avoided."
- BS 8611's hazard list is an excellent starting point but **not exhaustive** — RoboTed identified *additional* hazards (Uncanny Valley, weak security, lack of transparency, unrepairability, unrecyclability).
- **Psychological risks are especially hard to quantify** — no agreed measures for over-trusting or the Uncanny Valley; cultural differences shift risk levels → don't rely on designer judgment alone: engage users representative of age/gender/ethnic diversity + psychologists/social scientists.
- ERA is **not one-time** — it must iterate through the product lifecycle; early in-house assessments should be shared with user groups in later trials.

**Methodology 3 — The Ethics Canvas:** a 60–90-minute workshop tool to brainstorm ethical impacts (the 9 boxes above) and then commit to concrete design changes. Use it as the *structure* of your essay's group discussion: fill boxes ①–⑧, then pick the **four most important impacts** for box ⑨ and describe actual design/organizational changes.

**Worked Task 1 (mutual shaping) & Task 2 (ERA) for the Autonomous Robot Fitness Coach brief** — the lecture's own exercise; model answers are in the Literature Synthesis and Lab Presentation Prep sections below.

### Literature Synthesis

**1) Šabanović, "Robots in Society, Society in Robots" (Int. J. Social Robotics, 2010) — the mutual-shaping manifesto.**
- **Method:** participant observation + interviews with robotics researchers in the **US and Japan, 2005–2007** (NSF grant SES-0522630).
- **Finding:** the dominant discourse in robotics is **technologically determinist** — a linear view: scientific discovery → technological implementation → societal adoption, where "science finds, industry applies, man conforms." Social impact is assumed to derive from technical capability; society is a *passive receptor*.
- **The TD narrative in action (evidence the paper marshals):** robots framed as "technological fixes" for social problems (isolation, aging) — the analysis of social context serves only to justify new technical capabilities; users are "objects to be computationally described", not knowledge co-producers. Examples quoted: Bill Gates' "a robot in every home"; ASIMO sold on raw capability ("camera eyes at the right height…"); Wabot House — an environment engineered *for* the robot; researchers assuming adoption "just like the PC."
- **The alternative — mutual shaping / co-production:** technology and society produce each other; design always encodes *social and cultural choices* that "loop back to change the very terms in which we think about ourselves" (Jasanoff). Social robotics becomes a **wicked problem**: no linear progression, no exhaustive rules, multiple explanations, designer bears full responsibility.
- **Design recommendations extrapolated (two pillars, memorize):**
  - **Situating robot design in society:** evaluate robots in the wild ([1A]; e.g., GRACE's "social tag" study at AAAI05, where open-ended real-world interaction overturned lab assumptions — people interacted in groups, not one-on-one); study socio-technical ecologies before & after deployment ([1B]; e.g., ethnographic study of elders' domestic ecologies producing design recommendations; Roomba studies where cleaning became a *social* practice — teenagers and males started participating once the robot was involved); combine into **outside-in design** ([1C]; e.g., shadow-puppetry robot designed from coded observations of human-human interaction).
  - **Involving society in robot design:** stakeholders with tacit domain knowledge must influence design early ("socially robust, rather than merely acceptable"); participatory/collaborative robotics (e.g., Neighborhood Nets, where community members *become designers* and researchers become users); requires **polycentric, interactive, multipartite knowledge-making** and reflexivity.
- **Essay-useful quotable:** "In their emphasis on technological advancement as the determinant of societal success, roboticists define the societal issues they wish to solve 'not [as] social, political, cultural, historical problems, but [as] biotechnological problems that call for biotechnological solutions.'"

**2) Winfield & Winkle, "RoboTed: a case study in Ethical Risk Assessment" (ICRES 2020) — the ERA how-to.**
- **Contribution:** defines ERA (extending safety risk assessment's envelope to ethical risks), situates it in Responsible Robotics, and demonstrates it on a fictional robot teddy bear.
- **Theoretical anchor:** BS 8611 (2016) — first explicitly ethical robotics standard; guidance (not code of practice) for doing ERA; 20 hazards/4 categories (Societal incl. anthropomorphisation, loss of trust, deception, privacy/confidentiality infringement, addiction, loss of employment; plus Application, Commercial/Financial, Environmental); each with mitigation + verification/validation advice. Safety-standard lineage: ISO 14971 (medical devices), ISO 12100 (machinery).
- **Empirical outcome (the "so what" for your essay):** the ERA produced concrete design changes across physical, psychological, privacy/security and environmental risks — see the four tables above. The paper's own list: ERA can suggest new functions, modify designs, demand user engagement, and reject functionality.
- **Constraints to cite:** ERA is subjective & incomplete; BS 8611 is non-exhaustive; psychological risks lack agreed measures and vary culturally; ERA must iterate across the product lifecycle with diverse users and psychology/social-science expertise. ERA = design-time counterpart of **robot accident investigation** (ethical black box).

**3) The Ethics Canvas (ADAPT Centre / Trinity College Dublin & DCU, v1.8, 2017).**
- A **workshop tool** (adapted from Osterwalder's Business Model Canvas, CC BY-SA 3.0) for brainstorming the ethical impacts of a product/service and *committing to changes*.
- Purpose in the course: it operationalizes "embracing ethics as an engineer" — instead of a tick-box, it forces design-level responses (change the product, change the organization, add usage recommendations, or make values explicit).
- Process: fill Individuals affected → Groups affected → Product/Service Failure → Problematic Use of Resources → Worldviews → Group Conflicts → Relations → Behaviour; then box ⑨ **"What can we do?"**: select the **four most important** ethical impacts and redesign accordingly.

**4) The BS 8611 Hazard Table PDF (`HazardsTable.pdf`) — integrity note.**
- ⚠️ **The copy of `HazardsTable.pdf` in the course folder is corrupted**: it was produced by "Microsoft: Print To PDF" with a broken font mapping — it contains **no extractable text layer, no embedded fonts**, and renders as unreadable symbol glyphs (verified programmatically: `pdftotext`/`mutool` extract nothing; 300-dpi OCR yields garbage). It cannot be read even visually.
- **What it *should* contain** (verified against the lecture slides, the RoboTed paper, and BSI's official page): BS 8611's hazard-identification table — **20 ethical hazards grouped in 4 categories: Societal · Application · Commercial/Financial · Environmental** (each row: hazard, description, mitigation, verification/validation). The six societal hazards named in the sources are: **anthropomorphisation, loss of trust, deception, infringements of privacy & confidentiality, addiction, loss of employment**.
- **Action item:** download a clean copy of the table from the Canvas module (the slides there may have a readable version) — and cite the structure above, which is safe for quizzes and the essay.

### Lab Presentation Prep (this module = the essay + every future lab's ethics section)

1. **"Ethics is an engineering method, not a constraint" opener:** when presenting your essay conclusions or any lab design, argue that ERA + mutual shaping produce *better* systems (RoboTed's four concrete outcomes) — this reframing is the lecture's central rhetorical move and examiners reward it.
2. **Justify methodology choices with the terminology:** say explicitly "we took an *outside-in design* approach: [1B] context study → [1A] in-the-wild evaluation → iterate" or "we used *expert-in-the-loop IML as participatory design* because domain experts hold tacit knowledge our team lacks." Name the technique, then the reason.
3. **Run a live mini-ERA (60 seconds) for your lab artifact:** pick 2–3 hazards from the BS 8611 categories relevant to your system (e.g., for a health-related RL agent: psychological harm from wrong advice, privacy of user data, lack of transparency/logs) and state likelihood + mitigation. Even one slide of this signals the course's highest-level skill: *applying* standards.
4. **Pre-empt the standard limitations question:** psychological-risk measurement (no agreed scales), cultural variance, ERA subjectivity, non-exhaustiveness of BS 8611, and the need for iterative assessment — name them *before* the audience asks.
5. **Model answers for the Fitness-Coach tasks (rehearse these):**
   - *Task 1 (mutual-shaping pipeline):* study the context first (observe NHS group sessions; interview physiotherapists/runners at all programme stages) → participatory design with the domain expert (co-design robot actions, teaching interface, IML teaching in situ) → deploy in a real gym → iterate design with feedback. Watch out for TD traps: don't assume the app's design transfers to a robot; don't let only engineers decide.
   - *Task 2 (ERA):* hazards include **psychological harm** (robot pushing users past safe exertion → injury; users feeling judged/monitored), **deception/over-trusting** (users attributing medical authority to a robot), **privacy** (health/performance data), **addiction/dependence** (compulsive exercise), **product failure** (wrong instructions mid-session). Mitigations: expert-in-the-loop safety oversight, transparent non-medical framing, local data processing/deletion, rest-day limits ("sleep" analogue), an ethical black box log.

---

## Lecture 3: Search

### TL;DR

Problem solving via search: a problem has **4 components** — an initial state, a successor function (new_state = f(old_state, action)), a goal test, and a path-cost specification. The state space is everything reachable from the initial state; a solution is a *sequence of actions*; an optimal solution has minimum path cost. Every search algorithm in the lecture is the same generic loop — take a node out of a container, goal-test it, put its successors in — and the algorithm is defined entirely by the container discipline: FIFO queue gives BFS, LIFO stack gives DFS, priority queue on h gives greedy best-first, priority queue on g+h gives A*.

The second half covers what makes search practical: informed search steers with a heuristic h(n) (estimated cost from n to the goal), and A* is optimal when h never overestimates (admissible). When the *path* doesn't matter — only the final configuration (train schedules, N-queens, factory layouts) — local search keeps just one current state: hill climbing and its variants, plus simulated annealing. For the course, this lecture plus Lecture 4 *is* the Search assignment and the first on-campus quiz topic: you must be able to state each algorithm's completeness/optimality/time/space, hand-trace A* and greedy on the Romania map, and argue why a heuristic is admissible.

### Quiz Flash-Facts & Vocabulary

**Problem formulation (know cold):**
- **4 components of a search problem:** initial state · successor function · goal test · path-cost specification.
- **State space:** the set of all states reachable from the initial state.
- **Solution:** a sequence of actions; **optimal solution:** the one with minimum cost.
- Canonical examples: **routing** (initial state Arad, goal test "is the state Bucharest?", cost = distance traveled); **8-puzzle** (cost = number of moves); **8-queens** (initial state = empty board, successor = add one queen, ideally one column at a time, goal = no queen under attack, cost = 1 per placement/movement).

**Complexity parameters (every properties question uses these):**
- **b** = branching factor (max successors of any node) · **d** = depth of optimal solution · **m** = maximum length of a path in the state space (can be ∞).

**Uninformed search — the property table HT25 quizzes permute:**

| Algorithm | Container | Complete? | Time | Space | Optimal? |
|---|---|---|---|---|---|
| **BFS** | FIFO queue | Yes | O(b^d) | O(b^d) — keeps all nodes | Not in general (yes for uniform step costs) |
| **DFS** | LIFO stack | No — fails in spaces with loops (graph-search DFS is complete on finite graphs) | O(b^m) | O(bm) — linear | No |
| **Depth-limited** | LIFO + limit l | No if l < d | O(b^l) | O(bl) | No |
| **IDS** | repeated depth-limited, l = 0,1,2,… | Yes | O(b^d) | O(bd) | Under the same conditions as BFS |
| **Greedy best-first** | priority on h(n) | Only with repeated-state checking (loops) | O(b^m) — a good h helps a lot in practice | O(b^m) | No |
| **A\*** | priority on f(n) = g(n) + h(n) | Yes | Exponential in solution length | Keeps all nodes — **memory is the main problem** | Yes, if h is admissible |

- **Tree vs graph search:** graph search remembers visited states (an explored set) and adds children only if not already visited. Implemented with a **hash table** for near-constant-time lookups: index = hash_function(key) % N. **Zobrist hashing** is the common choice in games.
- **IDS overhead is small — know the numbers:** nodes in depth-limited search to depth d: N_DLS = b⁰ + b¹ + … + b^d; IDS: N_IDS = (d+1)b⁰ + d·b¹ + … + 1·b^d. For **b = 10, d = 5: N_DLS = 111,111 vs N_IDS = 123,456 → 11% overhead**. The repeated re-expansion is cheap because most nodes are near the leaves.
- **Bidirectional search:** search start→goal and goal→start simultaneously; motivation b^(d/2) + b^(d/2) ≪ b^d (two small circles vs one big). Difficulties: needs a **predecessor function** (not just successor) and explicit **goal states** (not just a goal test).

**Informed search:**
- **Best-first search** is the general form: expand low-cost nodes first, guided by an evaluation function f(n).
- **h(n)** = estimated cost of the cheapest path from node n to the goal. Example used throughout: straight-line distance to Bucharest.
- **Greedy best-first:** f(n) = h(n) — ignores the cost so far, only looks at what seems best from here. That's its flaw; A* fixes it by adding g(n).
- **A\*:** f(n) = g(n) + h(n), where g(n) = cost from start to n, f(n) = estimated total cost of the solution through n. Still the standard best-first method in robot navigation, autonomous driving, game AI, warehouse logistics, drone flight.
- **Admissible heuristic:** never overestimates the true cost to the goal. A* is optimal iff h is admissible.
- **A\* with h(n) = 0 is Uniform-Cost Search (Dijkstra)** — f(n) = g(n), still optimal. Favorite "what algorithm is this?" trap.
- **Memory-bounded A\* variants (know the names, details deferred to the book):** IDA* (iterative deepening A*), RBFS (recursive best-first search), MA*, SMA*.

**Heuristic design:**
- **8-puzzle classics:** h₁ = number of misplaced tiles; h₂ = sum of city-block (Manhattan) distances of tiles from their goal positions.
- **Dominance:** if h₂(n) ≥ h₁(n) for all n, h₂ **dominates** h₁ and expands fewer nodes — dominating heuristics are better, *as long as they stay admissible* (overestimate and you lose optimality).
- **How to invent heuristics:** solve **relaxed problems** (drop constraints — h₁ and h₂ are both relaxations of the 8-puzzle's move rules), analyze **sub-problems**, use **pattern databases**.

**Local search (path doesn't matter):**
- Use when the goal configuration itself is the solution: train schedules, factory-floor layout, N-queens. Keeps only a single current state; not systematic, but tiny memory and often finds reasonable solutions.
- **Hill climbing:** "find the top of Mount Everest in a thick fog while suffering from amnesia" — greedy local search, always move to a better neighbor. 8-queens heuristic: h = number of attacking queen pairs (slide example: h = 17; a local minimum at h = 1 that no single move improves).
- **Variants:** **stochastic** hill climbing (pick randomly among improving successors) · **first-choice** (generate successors randomly until one improves — good for huge branching) · **random restart** (repeat from random initial states until solved).
- **Simulated annealing:** occasionally accept a *bad* move to escape local optima; reduce the frequency/size of bad moves over time.

### Core Methodologies / Theories → Lab Relevance

**1) The generic search algorithm — one loop, five algorithms.**
- Tree search: put the root in the container; loop { container empty → FAIL; take a node out; goal-test it; add children }. Graph search adds: record the taken node's state; skip already-visited children.
- The whole taxonomy is the container: FIFO → BFS, LIFO → DFS, priority(h) → greedy, priority(g+h) → A*. When the quiz (or your oral exam) asks "why is BFS optimal for the 8-puzzle but not for the Romania routing problem?", the answer is step costs: BFS is optimal in *number of steps*, which equals cost only when all steps cost the same.
- In the Search assignment, "which container discipline do I use and why" is a legitimate design question — be ready to justify it with the property table above.

**2) Heuristics are where the grade is.** The algorithm skeleton is 20 lines; the heuristic decides whether it solves anything. For any heuristic you write, be able to answer: (a) Is it admissible? Prove it by identifying which problem constraint you relaxed. (b) Does it dominate the obvious alternatives? (c) What does it cost to compute per node — an expensive h can lose to a cheap one even with fewer expansions.

**3) Hand-tracing skill (this is exactly what the quiz tests).** Practice on the Romania map: greedy best-first from Arad goes Arad → Sibiu (h=253) → Fagaras (h=178) → Bucharest — cost 140+99+211 = 450, **not optimal** (the optimal path via Rimnicu Vilcea and Pitesti costs 418). A* with straight-line distance finds the optimal path because the heuristic is admissible (straight line never overestimates road distance). Also know the failure mode: tree-search greedy *without* repeated-state checking can oscillate forever (e.g., Iași ↔ Vaslui once the heuristic leads into a dead end) — this is why the completeness row says "only with repeated-state checking."

**4) Local search for configuration problems.** If your problem has no meaningful "path" (an N-queens board, a schedule), systematic search wastes memory storing paths. Hill climbing keeps O(1) state; its failure modes are local maxima, plateaus, and ridges — and the remedies are the three variants plus simulated annealing. Know which remedy addresses which failure mode: random restarts escape local optima globally; stochastic/first-choice handle huge or plateaued neighborhoods; annealing escapes by controlled downhill moves.

### Literature Synthesis

No separate reading assigned with this lecture — the content is Russell & Norvig's search chapters (the slides defer the memory-bounded A* variants IDA*/RBFS/MA*/SMA* to "the book"). The worked geography is the classic Romania map (Arad → Bucharest) with the straight-line-distance heuristic table, reused across greedy, A*, and UCS traces.

### Lab Presentation Prep (Search assignment + oral exam)

1. **Justify the algorithm, not just the code:** "we used A* because our heuristic is admissible — it relaxes [constraint], so it can never overestimate — and greedy gave us no optimality guarantee" beats "we used A* because it's standard."
2. **Have the property table memorized as a decision procedure:** complete? optimal? memory? Time? Examiners pick a scenario ("finite graph, unit costs, tight memory") and expect you to eliminate algorithms out loud (→ IDS).
3. **Pre-empt the memory question:** A*'s weakness is space — know the escape hatches by name (IDA*, RBFS, SMA*) and that IDS trades ~11% time overhead for O(bd) memory.
4. **If you used any local search:** name its failure mode you actually hit (local optimum/plateau) and the variant you used to escape it. "Random restarts because we kept landing in local minima" shows the theory drove the design.
5. **Quiz logistics from the lecture:** the in-classroom quiz the week after this lecture covers **both Search and Adversarial Search**; the Search assignment (Canvas + Kattis) has its grade-A deadline on **23 November, 19:00**, and the **individual learning journal is required from every student, including those working in pairs** — code and journal together determine the grade and feed the oral-exam questions. Full cross-reference: Part II, **Q1 Search**.

---

## Lecture 4: Adversarial Search

### TL;DR

Search with an opponent. Some problems are multi-agent; competitive ones are adversarial search problems, a.k.a. games. The lecture scopes itself to **turn-taking, two-player, zero-sum games with perfect information** and builds the standard stack: model the game as a tree (MAX levels and MIN levels), compute the best move with the **minimax** algorithm (assume an infallible opponent), cut off deep search with a heuristic **evaluation function**, and make the search feasible with **α-β pruning** — which returns exactly the minimax answer while skipping branches that can't affect it. Extensions covered: chance nodes (expectiminimax) for dice/card-luck games, and a deal-averaging approximation for imperfect-information games like cards.

Why games at all: precise rules, limited actions, and they're *hard* — chess has branching factor ~35 and ~50 moves per player, so 35¹⁰⁰ ≈ 10¹⁵⁴ nodes against ~10⁸⁰ atoms in the observable universe. You cannot search to the end; the whole lecture is about searching *well enough*. This lecture is the second half of the Search assignment's theory (the tutorial, summarized below, is titled "Search in Games" and walks minimax → α-β → heuristics → IDS → move ordering in exactly assignment order) and the second half of the upcoming in-classroom quiz.

### Quiz Flash-Facts & Vocabulary

**Game taxonomy and milestones (favorite trivia questions):**
- **Perfect information = fully observable.** Chess: perfect information, deterministic. Backgammon: perfect information **+ chance** (dice) — and the **first game where a computer defeated a human world champion**. Card games (poker etc.): **imperfect information** — you can't see the opponent's cards.
- **Chess:** Deep Blue beat Garry Kasparov in a six-game match **1997**; searched **200 million positions/second**; some lines extended to **40 ply**.
- **Checkers:** **solved in 2007** — 18 years of computation on a 15+ machine cluster, producing an endgame table for ≤10 pieces with **39 trillion entries**.
- **Go:** branching factor **b > 300** killed brute force. **AlphaGo's recipe:** supervised learning from human expert games trains a policy network → reinforcement learning via self-play improves it → deep networks guide **Monte Carlo Tree Search**, biasing and pruning exploration.
- Chess scale: **35¹⁰⁰ ≈ 10¹⁵⁴ nodes**; the observable universe has 10⁷⁸–10⁸² atoms.

**Formalization:**
- Players **MAX** and **MIN**; a game is defined by an **initial state**, a **successor function** (move, state), a **terminal state/test**, and a **utility (payoff) function** on terminal states, typically (+1, −1, 0).
- **Zero-sum:** the winner's gain equals the loser's loss (tutorial formalization: Σᵢ ψ(s, pᵢ) = 0; chess: win +1, loss −1, draw 0).
- **Optimal strategy:** at least as good as any other strategy against an **infallible** opponent. Key contrast with normal search: reaching the goal isn't enough — MAX must reach it *regardless of what MIN does*.
- 2-ply example from the slides: MAX's actions a₁/a₂/a₃ lead (under MIN's best replies) to values 3, 2, 2 → **play a₁**. If MIN is *not* infallible the minimax choice can be suboptimal in expectation, but minimax never assumes mistakes.

**Minimax:**
- MAX nodes take the **max** of child values, MIN nodes the **min**; terminal utilities propagate up. Assumes rational, self-interested players; gives the best achievable payoff against best opposing play.
- **Complexity O(b^m)** — full-tree analysis is usually impossible.
- **Repeated states:** different move orders reach the same position (**transposition**) → store evaluations in a **transposition (hash) table**.

**Cutoff and evaluation:**
- When depth runs out, a **heuristic evaluation function** estimates the position's value. It should: order cutoff states in a way that reflects their true expected utility, be **fast to compute**, and use **features relevant to winning** (chess: material — white/black pawns, queens, etc.).
- Cutoff test *in addition to* the terminal test; combined with **iterative deepening** for time control (tutorial: search 0→d, then 0→d+1, … until resources run out — beats a fixed depth that's either too shallow or too deep).

**α-β pruning (the algorithm this course drills hardest):**
- Prune branches that cannot affect the minimax result — **the answer is identical to minimax, computed with less work**.
- **α** = best value MAX can already guarantee on the path so far (a **lower bound**); **β** = best value MIN can guarantee (an **upper bound**). Initialized α = −∞, β = +∞ (tutorial convention).
- Propagation rules (tutorial, memorize): α and β are **only passed down the tree**; **α updates at MAX nodes, β updates at MIN nodes**; **prune when β ≤ α** — at a MAX node, value v ≥ β is a *beta cut* (MIN would never let the game get here); at a MIN node, v ≤ α is the symmetric cut.
- **Move ordering matters enormously:** with perfect ordering α-β examines **O(b^(m/2))** nodes — **twice the search depth for the same time**. Ordering heuristics: try likely-best moves first; in chess, captures → threats → forward moves → backward moves; estimate with a limited DFS; repeat **killer moves**.
- Ordering affects **efficiency only, never correctness** — arbitrary ordering still returns the optimal decision, just with less pruning.

**Beyond the deterministic core:**
- **Expectiminimax** for chance games (backgammon, Monopoly): insert **chance nodes** between MAX and MIN layers that take the **probability-weighted average** of their children instead of max/min.
- **Imperfect information** (cards): compute a probability for each possible deal; simple approximation = compute the minimax value of each action *in each deal*, then pick the action with the highest **expected value over all deals**.

**Tutorial ("Search in Games") implementation checklist — in this order:**
1. Make sure **minimax** works. 2. Make sure **α-β pruning** works. 3. Make sure your **heuristic** works as intended (positive = good for MAX, negative = good for MIN; cheap to compute). 4. Add **iterative deepening**. 5. Add **move ordering** (from heuristic values, transposition-table values, or the previous IDS iteration's results). 6. Check for **repeated states**. 7. Then explore extras: endgame lookup tables, killer moves.

### Core Methodologies / Theories → Lab Relevance

**1) Minimax as recursion.** The algorithm is a two-line mutual recursion (max-value / min-value) over the game tree. The lecture explicitly warns: *make sure you know how to work with recursive functions*. Trace small trees by hand until the value flow is mechanical — the quiz gives you a tree and asks for the value at the root or which branch gets pruned.

**2) α-β as window passing.** Think of [α, β] as a window of "values that can still matter," narrowed as the search descends: MAX nodes can only raise α, MIN nodes can only lower β, and when the window closes (β ≤ α) the remaining siblings are irrelevant. Practice the slide's worked tree (root actions a₁, a₂, a₃; MIN replies b₁…d₃; leaves −1/1/0) both in the given order and reordered, and watch which subtrees die. The reordering comparison is the whole point of the "does order matter?" slides.

**3) This is the Search assignment's engine room.** The tutorial deck is effectively an assignment walkthrough: the checklist above is the intended build order, and each step is independently testable — get minimax right before layering α-β on top, and verify α-β by checking it returns *the same move* as plain minimax on small trees (that's the invariant; the speedup is the only thing that should change). Iterative deepening + move ordering is how you survive a per-move time limit: the completed shallow search orders the moves for the next, deeper one.

**4) Evaluation functions under zero-sum.** Your heuristic is a stand-in for the true utility at the cutoff, so it must be *cardinally* sane, not just rank-ordered: positive favors MAX, negative favors MIN, magnitude should track how winning the position is. Feature-based (material counts, mobility, control of key squares/cells) keeps it cheap — a heuristic that costs more than the search it saves is a net loss.

### Literature Synthesis

No standalone reading assigned; the lecture's "literature" is the landmark game-playing systems, which double as quiz trivia and as design case studies:
- **Deep Blue (1997):** brute force + hardware — 200M positions/s, selective extensions to 40 ply. Proof that search depth wins chess.
- **Chinook/checkers (solved 2007):** search + a 39-trillion-entry endgame database — proof that some games yield to exhaustive precomputation.
- **AlphaGo (Go, b > 300):** when the branching factor defeats enumeration, replace breadth with learned intuition — policy/value networks trained by supervised learning then self-play RL, embedded in Monte Carlo Tree Search. This is the bridge to the course's later RL lectures.

### Lab Presentation Prep

1. **Show the invariant:** "our α-β returns the identical move to minimax on every test position, and here is the node-count reduction" — that sentence demonstrates both correctness and understanding of what pruning preserves.
2. **Explain your evaluation function feature by feature:** what each term measures, why it correlates with winning, and why it's cheap. Pre-empt "why not a deeper search instead?" with the O(b^(m/2)) argument — good ordering doubles effective depth, a better heuristic raises the value of every depth.
3. **Justify move ordering and IDS as one mechanism:** the previous iteration's best move is searched first in the next iteration, which is exactly the "perfect ordering" α-β wants — the two techniques compound.
4. **Know the scope boundary:** minimax assumes an infallible opponent and perfect information; if asked about cards or dice, the answers are deal-averaging and expectiminimax respectively. Volunteering the boundary shows you know where the method stops.
5. **Quiz cross-reference:** Part II, **Q2 Adversarial Search** — HT25's actual questions (α-β returns the same move as minimax; chess = perfect information + deterministic; zero-sum utility arithmetic; MIN node of [5, 2, 7, 4] → 2; ordering affects efficiency not correctness) are all settled by this lecture's content.

---

## Part II — Quiz-Targeted Revision (built from the HT25 Canvas quizzes)

> The five HT25 Canvas quizzes in `LastQuizzes/` are the best available predictor of this year's quiz style: 4–6 questions, 60 minutes, **5 attempts, correct answers hidden**. Each module below lists what HT25 actually asked, the theory needed to answer it, and the trap pattern in the distractors. Topics seen in HT25: **Q1 Search, Q2 Adversarial Search, Q4 Machine Learning, Q9 Logic, Q10 Planning**. The PDFs for Q3 and Q5–Q8 were not preserved; they are **reconstructed below** from the DD2380 topic spine and Russell & Norvig, in the observed HT25 style (definition questions, swapped-definition distractors, one hand-computation per quiz). The reconstruction assigns: **Q3 CSP, Q5 Bayesian networks, Q6 HMMs, Q7 MDPs, Q8 Reinforcement learning** — this matches the on-campus quiz topics (Search, HMMs, RL) and the gap dates in the attempt histories. Treat reconstructed questions as predictions, not recovered originals.

**Two strategic facts about the format:**
- Correct answers stay hidden after submission, so attempt 1 is reconnaissance: screenshot every question and option, solve them offline against these notes, and only spend attempts 2+ when confident. (HT25 evidence: Q1 went 3/5 → 3.5/5 → 5/5 across attempts.)
- Distractors here are mostly *swapped definitions* — DFS/BFS containers exchanged, g/h/f permuted, function/predicate flipped. Read every option to the end; the right answer is usually the one you can define from scratch, not the one that sounds familiar.

### Q1 Search — what HT25 asked

> Full theory module: **Lecture 3: Search** above (property tables, heuristic design, Romania-map traces).

1. **Successor function:** "a function that tells which new state a certain action leads to from a given state." Distractors redefined it as a probability (that's a stochastic transition model), a cost list (that's the step-cost function), or a predecessor map (backwards).
2. **Containers:** DFS = **stack (LIFO)**; BFS = **queue (FIFO)** — BFS continues from the node added *first*. The wrong options swap the two.
3. **BFS Bucharest → Sibiu (Romania map):** BFS is optimal in *number of steps*, so it returns **Bucharest–Fagaras–Sibiu (2 edges)**, not the 3-edge route via Pitesti and Rimnicu Vilcea. The "infinite loop between Fagaras and Bucharest" option is false *if* you keep an explored set (graph search); tree search without loop checking genuinely can cycle — know which variant you mean.
4. **Greedy best-first search:** expand the node with the lowest **h(n)** (estimated cost from n to goal). Distractors: lowest **g(n)** alone (uniform-cost search) and lowest **f(n) = g(n) + h(n)** (A*).
5. **Hill climbing, 8-queens:** heuristic = number of attacking queen pairs; move the queen whose best placement yields the lowest h. "No move is possible since h does not improve for all positions" is a legitimate answer shape — hill climbing halts at local minima and plateaus, so compute h for candidate moves before ruling it out.

**Theory to have cold:**
- A search problem = initial state + actions/successor function + goal test + step cost. A solution is a path from initial state to a goal state; optimal = lowest path cost.
- Frontier discipline decides everything: stack → DFS (depth-first, memory O(bm), neither complete nor optimal in general); queue → BFS (complete, optimal for uniform step costs, memory O(b^d)); priority queue → UCS/Greedy/A*.
- Decision rules: UCS orders by g(n), Greedy by h(n), A* by f(n) = g(n) + h(n). Quiz questions love permuting these three.
- Hill climbing is local search: no frontier, keep only the current state, move to the best neighbor, stop when no neighbor improves. Failure modes: local maxima/minima, plateaus, ridges; remedy = random restarts.
- **Admissible heuristic:** never overestimates the true cost to goal. **Consistent:** h(n) ≤ c(n,a,n′) + h(n′) for every successor n′; consistency implies admissibility, and A* with a consistent heuristic is optimal under graph search. Not in HT25 Q1, but standard on-campus material.

### Q2 Adversarial Search — what HT25 asked

> Full theory module: **Lecture 4: Adversarial Search** above (minimax, α-β windows, move ordering, expectiminimax).

1. **Alpha-beta pruning:** ignores branches that an optimal player will never choose — it returns *exactly the same move as minimax* while exploring fewer nodes. Distractors: "ensures MAX always wins" (no — minimax can't beat a lost position), "checks all nodes" (that's the opposite), "searches 10× deeper" (real bound: with perfect move ordering it examines O(b^(d/2)) nodes, i.e. up to **twice the depth** for the same budget).
2. **Chess classification:** **perfect information and deterministic**. Contrast set: backgammon (perfect information + chance), poker/Kriegspiel (imperfect information).
3. **Zero-sum games:** terminal utilities sum to a constant. MAX utility +5 ⇒ MIN utility **−5**, necessarily.
4. **MIN node with children [5, 2, 7, 4]:** returns **2** — the minimum. Every other option dresses up an averaging rule; MIN only ever takes the min.
5. **Move ordering:** with arbitrary (non-optimal) expansion order, alpha-beta **still guarantees the optimal decision** but may prune less and explore more nodes. Ordering affects *efficiency only, never correctness*. Best-first ordering gives maximal pruning.

**Theory to have cold:**
- Minimax: MAX levels take the max of child values, MIN levels the min, values propagate up from terminal utilities. The minimax decision assumes an optimal opponent.
- α = best (highest) value MAX can already guarantee on the path to the root; β = best (lowest) value MIN can guarantee. Prune a subtree when its value cannot beat the current α (at a MAX node) or β (at a MIN node).
- Too deep to exhaust → cutoff test + **evaluation function** (weighted linear features, e.g. chess material). Chance nodes → **expectiminimax**: replace max/min at chance levels with the probability-weighted average; note that expectiminimax values are not order-preserving, so evaluation functions must be cardinally meaningful.


### Q3 Constraint Satisfaction Problems — RECONSTRUCTED (no HT25 PDF preserved)

Placement logic: HT25's problem-solving block was Search → Adversarial Search → CSP (Russell & Norvig ch. 6), and the quiz release dates leave exactly one slot between Q2 (4 Nov) and Q4 (20 Nov).

**Predicted questions and answers:**

1. **What defines a CSP?** A set of **variables**, each with a **domain** of values, and **constraints** over subsets of variables. A solution is a **complete, consistent assignment** (every variable assigned, no constraint violated). Likely distractors: "an assignment that maximizes a heuristic" (that's optimization/local search), "a partial assignment" (incomplete).
2. **Backtracking search variable ordering:** **MRV** (minimum-remaining-values) picks the variable with the fewest legal values left — fail fast. Ties broken by the **degree heuristic** (most constrained variable). Value ordering uses **LCV** (least constraining value) — leave maximum freedom for neighbors. Distractor pattern: MRV and LCV swapped (MRV is for *variables*, LCV for *values*).
3. **Arc consistency / AC-3:** arc Xᵢ → Xⱼ is consistent iff **every** value in Dᵢ has *some* supporting value in Dⱼ satisfying the constraint; AC-3 removes unsupported values and re-enqueues affected arcs. Removing a value from Dᵢ can break arcs pointing *into* Xᵢ — that's why neighbors get re-checked. Know that arc consistency detects failure when a domain empties, but consistency alone does not prove a solution exists.
4. **Hand-trace question (map coloring or N-queens):** run forward checking one or two steps — after assigning a variable, delete conflicting values from *unassigned neighbors'* domains. Expect "which value is deleted from which domain next?" as the question shape.
5. **Min-conflicts:** local search for CSPs — start from a complete (random) assignment, repeatedly move one conflicted variable to the value that minimizes constraint violations. Surprisingly effective on N-queens; contrast with backtracking (systematic, complete) vs min-conflicts (incomplete, fast).

**Theory to have cold:**
- Constraint types: unary, binary, higher-order; any CSP can be converted to binary constraints only.
- Backtracking = DFS + one variable per level + legality check against assigned variables. Inference between assignments (forward checking, AC-3) prunes earlier than pure backtracking.
- Tree-structured CSPs solvable in linear time after directional arc consistency; general CSPs are NP-complete.

### Q4 Machine Learning — what HT25 asked

1. **Supervised vs unsupervised:** the supervised cases were the two with **labels for exactly what you predict** — text labeled by language → predict language; photos labeled smiling/not → recognize smiling. Clustering speech samples by speaker is unsupervised (no labels), and suggesting people to meet is a recommendation task, not labeled classification. Rule of thumb: if the training data contains the *answer you want the model to produce*, it's supervised.
2. **Choosing a regression curve by eye:** match the function family to the data's shape. Too rigid (straight line through curved data) = **underfitting**; a high-degree polynomial threading every point = **overfitting**.
3. **Least squares by hand** for y = wx + b: w = Σ(xᵢ − x̄)(yᵢ − ȳ) / Σ(xᵢ − x̄)², then b = ȳ − w·x̄. The four sign combinations of (w, b) are the distractor set, so sign errors are fatal — practice on a 3–4 point dataset and check the line passes through (x̄, ȳ).
4. **Model selection:** split into training and validation sets, train on the training part, pick the model with the lowest **validation** error. Distractors: select on training error (rewards overfitting), "always pick the simplest model", "always pick the most flexible model".
5. **Regularization:** adding a complexity penalty (e.g. λ‖w‖²) to the goodness-of-fit function **to avoid overfitting** — it discourages large weights that memorize noise. Distractors claimed it speeds up optimization, sets the polynomial degree, or converts the task to classification.

**Theory to have cold:**
- Supervised learning: given input–output pairs, learn a hypothesis h. Discrete output = **classification**, continuous output = **regression**. Unsupervised: no outputs given, find structure (clustering, dimensionality reduction). Reinforcement: learn from rewards, not labeled examples.
- Loss/goodness-of-fit: regression uses squared error (least squares); the optimum trades off fit against complexity once regularization is added.
- Overfitting = low training error, high test error; underfitting = high error on both. More data and regularization fight overfitting; a richer hypothesis class fights underfitting.
- Validation set (or k-fold cross-validation) estimates generalization; the test set is touched only once, at the end.


### Q5 Bayesian Networks — RECONSTRUCTED (no HT25 PDF preserved)

Placement logic: the "taming uncertainty" block (probabilistic reasoning → Bayesian networks → HMMs) fills the late-November gap between Q4 and Q9, and HMMs are an on-campus quiz topic, so their prerequisite (BNs) must precede them.

**Predicted questions and answers:**

1. **What does a Bayesian network encode?** A DAG where each node is a variable and each node carries P(node | parents); the network encodes the factorization **P(x₁,…,xₙ) = Πᵢ P(xᵢ | parents(Xᵢ))** and the conditional independencies that follow. Distractor: "a fully connected graph storing the full joint" — that defeats the entire point.
2. **The key independence:** a node is conditionally independent of its **non-descendants given its parents**. Stronger version: given its **Markov blanket** (parents + children + children's parents), a node is independent of everything else. Expect one question asking which set makes two variables independent.
3. **Parameter counting:** full joint over n Boolean variables needs **2ⁿ − 1** numbers; a BN where each node has at most k parents needs at most **n·2ᵏ**. Numeric variants (n=10, k=2) are likely — compute both and compare.
4. **Hand-computation with the classic alarm network** (Burglary, Earthquake → Alarm → JohnCalls, MaryCalls): compute P(B | J, M) or a joint entry by multiplying CPT rows. Method: P(x₁..xₙ) = product of each variable's CPT entry given its parents' values; for queries, enumerate hidden variables. Practice one full enumeration by hand.
5. **Inference complexity / d-separation:** exact inference is NP-hard in general but linear in **polytrees** (singly connected networks). Or: two nodes are d-separated given evidence if every path between them is blocked — know the three connection types (chain, fork, collider) and that a **collider blocks unless it or a descendant is observed** ("explaining away").

**Theory to have cold:**
- Semantics: the joint equals the product of CPTs; every conditional independence claim is read off the graph, not assumed.
- Chain rule + BN factorization → any joint entry is one product of CPT lookups.
- Inference by enumeration: P(query | evidence) ∝ Σ over hidden variables of the joint entries; variable elimination caches repeated sub-products.

### Q6 Hidden Markov Models — RECONSTRUCTED (no HT25 PDF preserved)

HMMs are an on-campus quiz topic in this course, so this reconstruction deserves the most care of the five.

**Predicted questions and answers:**

1. **The two assumptions:** the **Markov assumption** on states — P(Xₜ | X₀..ₜ₋₁) = P(Xₜ | Xₜ₋₁) (the future is independent of the past given the present) — and the **sensor Markov assumption** — P(Eₜ | X₀..ₜ, E₁..ₜ₋₁) = P(Eₜ | Xₜ) (evidence depends only on the current state). Distractors weaken these to "depends on the previous two states."
2. **The three tasks:** **filtering** = P(Xₜ | e₁..ₜ) (current state given evidence so far); **prediction** = P(Xₜ₊ₖ | e₁..ₜ); **smoothing** = P(Xₖ | e₁..ₜ), k < t (past state given all evidence). Know which is which — "estimating yesterday's weather given all of this week's umbrella observations" is smoothing, not filtering.
3. **The forward recursion (filtering), one step by hand:** P(Xₜ₊₁ | e₁..ₜ₊₁) ∝ P(eₜ₊₁ | Xₜ₊₁) · Σₓₜ P(Xₜ₊₁ | xₜ) · P(xₜ | e₁..ₜ) — i.e. **project forward through the transition model, then reweight by the new evidence, then normalize**. Expect a numeric question on the umbrella-world: given a 2×2 transition matrix and sensor model, compute the filtered belief after one observation. Practice until the two-step (predict → update) is mechanical.
4. **Smoothing = forward-backward:** P(Xₖ | e₁..ₜ) ∝ f₁..ₖ · bₖ₊₁..ₜ — forward message from filtering, backward message computed backwards through the evidence. Know the decomposition exists and what each message means.
5. **Viterbi / most likely explanation:** the most likely *sequence* argmax P(x₁..ₜ | e₁..ₜ) is found by a Viterbi-style max-product recursion, and it is **not** the same as picking the most likely state at each time step individually. That non-equivalence is the classic trap option.

**Theory to have cold:**
- An HMM = transition model P(Xₜ | Xₜ₋₁) + sensor model P(Eₜ | Xₜ) + prior P(X₀). It is the simplest **dynamic Bayesian network** — a BN unrolled over time with one state and one evidence variable per slice.
- All four tasks are instances of the same message-passing; filtering and prediction run forward, smoothing adds a backward pass, Viterbi replaces sums with maxes.
- Stationarity assumption: transition and sensor models are the same for all t.

### Q7 Markov Decision Processes — RECONSTRUCTED (no HT25 PDF preserved)

**Predicted questions and answers:**

1. **What defines an MDP?** States, actions, a **transition model** T(s, a, s′) = P(s′ | s, a), a **reward function** R(s) (or R(s,a,s′)), and optionally a discount γ. The Markov property: the next state depends only on the current state and action. Distractor: "the agent observes only part of the state" — that's a **POMDP**, the standard swapped-definition trap.
2. **The Bellman equation:** U(s) = R(s) + γ · maxₐ Σₛ′ T(s, a, s′) · U(s′). Know every symbol. The max makes it nonlinear — that's why you can't just solve it as a linear system for the *optimal* utility.
3. **Value iteration:** repeatedly apply the Bellman update Uᵢ₊₁(s) ← R(s) + γ maxₐ Σ T(s,a,s′)Uᵢ(s′) to every state; guaranteed to converge to U* for **γ < 1** (contraction). Policy extraction afterwards: π*(s) = argmaxₐ Σₛ′ T(s, a, s′) U(s′). Expect "given these utilities and transitions, which action is optimal in state s?" — one hand-computation.
4. **Policy iteration:** alternate **policy evaluation** (solve the linear system Uᵢ = U^πᵢ — linear because the max is gone once π is fixed) with **policy improvement** (greedy one-step lookahead); terminates when the policy stops changing. Know the contrast with value iteration: VI interleaves everything; PI separates evaluation from improvement.
5. **The discount factor:** γ ∈ [0,1) trades off immediate vs future reward and guarantees finite utilities for infinite horizons (geometric bound R_max/(1−γ)). Distractors: "γ > 1 for long-sighted agents" (diverges), "γ has no effect."

**Theory to have cold:**
- A policy π maps states to actions; the utility of π is the expected discounted total reward from following it. The optimal policy π* maximizes expected utility from every state.
- Sequential decision problems under uncertainty generalize search: outcomes are stochastic, so you optimize *policies*, not action sequences.
- Small negative step costs (living rewards) encourage reaching good terminal states quickly — the 4×3 gridworld is the canonical example.

### Q8 Reinforcement Learning — RECONSTRUCTED (no HT25 PDF preserved)

RL is an on-campus quiz topic and a lab, so expect this reconstruction to be close to the real thing.

**Predicted questions and answers:**

1. **How RL differs from supervised learning:** the agent learns from **rewards**, not labeled input–output pairs, and must act to gather data. Distractor: "RL is supervised learning with more data" — no; there is no teacher saying the correct action, only an evaluation of outcomes.
2. **The Q-learning update:** Q(s,a) ← Q(s,a) + α · [ r + γ · maxₐ′ Q(s′,a′) − Q(s,a) ]. Identify each term: α = learning rate, the bracket = **TD error**, r + γ max Q = the TD target. Q-learning is **model-free** and **off-policy** (it learns the greedy policy's values even while exploring). Likely numeric variant: plug in numbers for one update by hand.
3. **SARSA vs Q-learning:** SARSA's target uses the action **actually taken** next (on-policy): r + γ Q(s′, a′); Q-learning uses the **best** next action (off-policy). The swapped-definition distractor pair is near-certain.
4. **Exploration vs exploitation:** ε-greedy picks a random action with probability ε and argmaxₐ Q(s,a) otherwise; without exploration the agent can lock onto a suboptimal policy (the "greedy in the limit" fix: decay ε over time — GLIE).
5. **Passive vs active RL:** passive = fixed policy, learn only its utilities (TD learning: U^π(s) ← U^π(s) + α[r + γU^π(s′) − U^π(s)]); active = the agent chooses actions and must explore. Also: model-based (learn T and R, then solve with value/policy iteration) vs model-free (Q-learning/SARSA).

**Theory to have cold:**
- RL = learning in an MDP where T and R are unknown; the agent experiences transitions (s, a, r, s′).
- TD learning updates estimates from other estimates (bootstrapping) — no need to wait for episode end, unlike Monte-Carlo/ADI approaches.
- Convergence of Q-learning requires every state-action pair to be tried infinitely often and α decayed appropriately.

### Q9 Logic — what HT25 asked (4/6 — the weakest topic, prioritize it)

1. **Entailment algebra:** the options mixed ⊨ and →. The reliable facts: **transitivity** (α ⊨ β and β ⊨ γ ⇒ α ⊨ γ), **monotonicity** (α ⊨ β ⇒ α ∧ γ ⊨ β — adding premises never destroys entailment), and the **deduction theorem** (α ⊨ β iff α → β is valid). Check each candidate statement against the definition: α ⊨ β means β is true in *every model where α is true*.
2. **Propositional tautologies:** valid = true in every row of the truth table. Reliable examples: (P ∧ Q) → P; ¬(P ∧ Q) ↔ (¬P ∨ ¬Q) (De Morgan). Reliable non-examples: P → Q does not entail Q → P; (P → Q) ∧ P is not a tautology, though it *entails* Q (modus ponens is an inference rule, not a valid sentence by itself... check the exact form).
3. **Resolution rule:** from clauses (A ∨ B) and (¬B ∨ C) derive (A ∨ C) — cancel **one complementary literal pair**. Works only on clauses (CNF). Distractors resolve on two literals at once or cancel literals that aren't complementary.
4. **Predicate vs function (missed in HT25):** predicates map objects to **truth values**, functions map objects to **objects**. In a *sentence* like Foo(Bar(x)): Foo must be a **predicate** (the sentence has to be true or false) and Bar a **function** (it sits in an argument position, producing an object). Memorize: functions nest inside arguments; predicates wrap the outside.
5. **FOL validity:** ∀x P(x) → P(c) is valid (universal instantiation); the converse P(c) → ∀x P(x) is not. Watch quantifier order: ∀y∃x Loves(x,y) does not entail ∃x∀y Loves(x,y).
6. **Making "the parliament has at least one member" true in every model (missed in HT25):** a KB of pure universal rules (∀x PM(x) → GOV(x) etc.) has models where nothing satisfies anything — universals alone never create objects. You must add a **ground fact with a constant**: MP(Smith) directly, or PM(Smith) plus the chain PM → GOV → MP. The "no sentence needs to be added" option is the trap.

**Theory to have cold:**
- Syntax vs semantics: a **model** assigns truth/objects; α ⊨ β (entailment, semantic) vs KB ⊢ α (derivation, syntactic). An inference algorithm is **sound** if it derives only entailed sentences, **complete** if it derives all of them. Resolution is sound, and refutation-complete.
- CNF conversion: eliminate ↔ and →, push ¬ inward (De Morgan, double negation), distribute ∨ over ∧. Resolution refutation: to prove KB ⊨ α, add ¬α, convert to CNF, and derive the empty clause.
- FOL building blocks: constants (objects), functions (object → object), predicates (object(s) → truth value), ∀/∃ quantifiers. Instantiation: from ∀x P(x) infer P(anything); from ∃x P(x) introduce a *fresh* Skolem constant.

### Q10 Planning — what HT25 asked

1. **Well-defined PDDL action schemas (the one missed):** in the base STRIPS-style formalism, preconditions are conjunctions of **positive literals only** and effects are conjunctions of literals where a **negated literal is a delete effect**. So **NOT** well-defined in the basic formalism: a **disjunction in the precondition** and a **negation in the precondition** (both require extra requirements, e.g. ADL-style extensions). Perfectly legal: negation in the *effect* (that's how deletion works) and multiple literals in the effect (conjunction).
2. **Towers of Hanoi as PDDL:** verify a candidate action sequence by simulation — before each move, check the preconditions (disk clear, destination clear, disk smaller than whatever is beneath). One illegal move disqualifies the whole sequence.
3. **Relaxed-problem heuristic:** deleting a precondition removes constraints, so the relaxed problem's optimal solution costs **no more** than the original's → an **admissible** heuristic. Know the family: ignore-preconditions, ignore-delete-lists (h⁺, with the approximations h_add and h_max). The divided/multiplied-by-two distractors probe whether you've noticed an action that moves *two* items at once — counting misplaced items then over/underestimates by a factor of 2.
4. **Planning graphs:** S₀ = initial literals; Aᵢ = every action whose preconditions appear in Sᵢ; Sᵢ₊₁ = all effects of Aᵢ plus **no-ops** (literals persist). A literal first appears at the earliest level where some action (including a no-op) produces it from satisfiable preconditions. "Never" is a genuine option — if no action can ever produce the literal, it never appears. Goals must all appear **non-mutex** at a level before extraction is attempted.

**Theory to have cold:**
- State = conjunction of fluents (ground, function-free literals). Action schema = precondition + effect (add list / delete list). Plan = action sequence taking the initial state to a state satisfying the goal.
- Forward search (from initial state through applicable actions) vs backward search (regress from the goal through relevant actions); both are standard state-space searches and inherit their heuristics from relaxations.
- Mutex relations: two actions at a level are mutex if one deletes the other's precondition or effect (interference, competing needs); two literals are mutex if one is the negation of the other or all ways of achieving them are pairwise mutex.

---

## Appendix A — Source Inventory & Extraction Log (Step 1 confirmation)

| File | Pages/Size | Extraction | Status |
|---|---|---|---|
| `Lecture 1a - Introduction.pdf` | — | `pdftotext` → 10,160 chars | ✅ Clean text |
| `Lecture 1b - Course Practicalities.pdf` | — | `pdftotext` → 10,819 chars | ✅ Clean text |
| `Intro_AIEthics_Oct29.pdf` | 109 slides | `pdftotext` → 60,350 chars | ✅ Clean text |
| `Robotsinsociety.pdf` | Šabanović 2010 | `pdftotext` → 78,091 chars | ✅ Clean text |
| `Roboted.pdf` | Winfield & Winkle 2020 | `pdftotext` → 23,040 chars | ✅ Clean text |
| `EthicsCanvas.pdf` | 1 page | `pdftotext` → 5,773 chars | ✅ Clean text |
| `HazardsTable.pdf` | 4 pages, BS 8611 table | 4 chars; OCR = symbol garbage | ❌ Corrupted file — content cross-verified via lecture slides, RoboTed paper & BSI |
| `Lecture 3 - Search.pdf` | 99 slides | `pdftotext -layout` → `.extracted/Lecture3_Search.txt` | ✅ Clean text (map-trace slides filtered) |
| `Lecture 4 - Adversarial Search.pdf` | 59 slides | `pdftotext -layout` → `.extracted/Lecture4_AdversarialSearch.txt` | ✅ Clean text |
| `Search_Tutorial.pdf` ("Search in Games") | 16 slides | `pdftotext -layout` → `.extracted/Search_Tutorial.txt` | ✅ Clean text |

- **Tooling:** `extract_course_materials.py` (in this folder) wraps `pdftotext`/`pdftoppm` + a locally extracted tesseract; full log in `.extracted/_extraction_report.txt`.
- **Admin fluff discarded:** Mentimeter polls, room/logistics notices, email-address trivia, duplicate slides, and the slides' own navigation footers.

## Appendix B — Module Template for Future Lectures

Copy this skeleton whenever a new lecture's slides/readings land; keep sections in this exact order:

```markdown
## Lecture N: [Topic]

### TL;DR
[Paragraph 1: the lecture's core thesis, one or two sentences each on the main ideas.]
[Paragraph 2: how this connects to the labs/exams — what a student must be able to DO with it.]

### Quiz Flash-Facts & Vocabulary
- **[Term]:** [one-line definition; define before use]
- [Rapid-fire facts with numbers, years, and names in bold]

### Core Methodologies / Theories → Lab Relevance
[Break down the main method(s); for each: what it is, how to execute it, worked example, and exactly how it appears in the programming assignments.]

### Literature Synthesis
[For each assigned reading: author, year, method, key argument, and the specific data points/constraints that inform lab work.]

### Lab Presentation Prep
1. [Talking point 1: justification of a methodological choice]
2. [Talking point 2: limitation to pre-empt]
3. [Talking point 3: how to explain results to an audience]
```


> [PLACEHOLDER: FUTURE LECTURES TO BE APPENDED HERE]
