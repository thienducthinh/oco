# Lesson 9: Mental Models and Representations

In this lesson, we explore mental models and representations in Human-Computer Interaction (HCI), focusing on how they shape user understanding and interface design. The topics include:

1. **Mental Model**: An internal, simulatable understanding of external reality.
2. **Representations**: Internal symbols representing external reality.
3. **Metaphors and Analogies**: Tools to create effective representations.
4. **User Error**: Slips and mistakes arising from mental models.
5. **Learned Helplessness**: A consequence of poor interface design.
6. **Expert Blind Spot**: A reason why poor design may occur.

## Mental Model

A mental model is a user’s internal understanding of how a system works, including processes, relationships, and connections in real-world systems. It allows users to simulate events, predict outcomes, and check results. For example, in basketball, a player might mentally simulate a shot’s trajectory to predict its success.

- **When Reality Mismatches**: If the mental model doesn’t align with reality, users may feel discomfort, curiosity, frustration, or believe they’ll never understand the system.
- **Design Implications**: Interfaces should either match users’ existing mental models or teach new ones effectively. Good interfaces enable predictable and learnable interactions.
- **Beyond HCI**: Mental models are also relevant in fields like educational technology (EdTech), where they support learning without requiring standalone explanations.
- **Challenges**: Creating representations that accurately convey how a system works is difficult but critical for effective mental models.

**Example**: In a climate control system, David’s old and new cars had interfaces that confused him, highlighting the challenge of aligning interfaces with user mental models.

## 5 Tips: Mental Models for Learnable Interfaces

Based on Dix et al., the following tips help create learnable interfaces by supporting accurate mental models:

1. **Predictability**: Users should predict what will happen before acting.
2. **Synthesizability**: Users should understand how they reached the current state (e.g., command logs in a CLI).
3. **Familiarity**: Leverage actions users already know, similar to affordances.
4. **Generalizability**: Knowledge from one interface should apply to others.
5. **Consistency**: Ensure actions (e.g., Ctrl+X for cut) remain consistent across contexts.

## Representations

Representations are internal symbols or external cues that help users understand and interact with a system. They are crucial for creating effective mental models.

- **Role in Design**: Designers choose how to present information to users, ensuring representations align with real-world tasks.
- **Example**: Cat furniture vs. office furniture illustrates good mapping between mental models and real-world objects.
- **Purpose**: Representations should simplify complex systems and enhance understanding.
- **Simple Problems**: Easier to create effective representations for straightforward tasks.

### Characteristics of Good Representations

Good representations exhibit the following traits:

1. **Depicts Explicit Relationships**: Clearly shows connections between elements for easy understanding.
2. **Brings Objects and Relationships Together**: Makes objects and their interactions explicit.
3. **No Extraneous Information**: Avoids irrelevant details (e.g., specifying only left-to-right navigation).
4. **Exposes Natural Constraints**: Incorporates environmental or contextual cues to guide user actions.

## Analogies and Metaphors

Analogies and metaphors ground interfaces in familiar concepts, making them more learnable:

- **Benefits**: By relating the interface to something users already know (e.g., a Wall Street website resembling a newspaper), designers provide a solid foundation for learning.
- **Challenges**: Users may not recognize where the analogy ends, leading to misconceptions. Analogies can also impose outdated constraints, limiting interface innovation.
- **Example**: A newspaper metaphor for a financial website aids learnability but may restrict modern design possibilities.

## Design Principles Revisited

Mental models and representations tie into core HCI design principles:

- **Analogies and Metaphors**: Align with the principle of

# Lesson 10: Task Analysis

In this lesson, we explore two primary methods for task analysis:

1. **Human Information Processor Models** - Focus on models like the GOMS Model, treating the user as a processor with inputs and outputs (Processor Model).
2. **Cognitive Task Analysis** - Emphasizes internal thought processes, such as memory and attention, to predict user behavior (Predictor Model).

## GOMS Model

The **GOMS Model** (Goals, Operators, Methods, Selection Rules) is a human information processor model that builds on the concept of a human's role in a system. It consists of four components:

1. **Goals**: What the user aims to achieve.
2. **Operators**: Basic actions the user performs to execute a method.
3. **Methods**: Sequences of operators to accomplish a goal.
4. **Selection Rules**: Criteria or rules used to choose one method over another.

The model assumes a user has a set of goals and selects from available methods, each composed of operators, to achieve those goals. Selection rules guide the choice of method.

*Example*: To transfer information to coworkers, a user might choose methods like email, chat, or in-person communication.

### Strengths of GOMS Model

1. **Formalizes User Interaction**: Breaks down interactions into measurable steps, enabling efficiency analysis and identification of improvement areas (e.g., timing each operator, such as retrieving a keychain while holding an object).

### Weaknesses of GOMS Model

1. **Does Not Address Complexity**: Standard GOMS overlooks complex methods and sub-methods.
2. **Assumes Expert Users**: Does not account for novices or user errors (e.g., unfamiliarity with a system like navigating highways in the USA).

### Types of GOMS

1. **KLM-GOMS (Keystroke-Level Model)**:
   - Focuses on operators and their execution times to determine efficiency.
   - Originally defined six operator types, less applicable to modern interfaces.
2. **CMN-GOMS (Card, Moran, and Newell GOMS)**:
   - Supports hierarchical goals, including low-level tasks (e.g., moving text, deleting phrases).
   - Estimates time for individual GOMS components to identify inefficiencies.
3. **NGOMSL (Natural Language GOMS)**:
   - Incorporates working memory and lends itself to human interpretation.

### 5 Tips for Developing GOMS Models

1. **Focus on Small Goals**: Start with small, specific goals (e.g., navigating to the end of a document) and abstract upward.
2. **Nest Goals, Not Operators**: Break down goals hierarchically (e.g., navigation includes sub-goals like changing lanes), but keep operators as the smallest units.
3. **Differentiate Descriptive vs. Prescriptive**: Descriptive models (what users do) may not predict prescriptive actions (what they want to do).
4. **Assign Costs to Operators**: Measure the time or effort each operator requires.
5. **Use GOMS to Trim Waste**: Reduce costs by eliminating unnecessary operators.

## Transition from GOMS to Cognitive Task Analysis

The GOMS model simplifies humans as input-output machines (processor model). However, human reasoning is often too nuanced for such simplification. **Cognitive Task Analysis (CTA)** addresses this by focusing on internal processes like memory, attention, and cognitive load (predictor model).

- **Behaviorism vs. Cognitivism**:
  - Behaviorism emphasizes observable actions (stimuli and responses).
  - Cognitivism focuses on internal thought processes (cognition, learning, memory).

## Cognitive Task Analysis

CTA is a collection of methods that examine the underlying thought processes involved in performing tasks. Most CTA methods follow a common sequence:

1. **Collecting Preliminary Knowledge**:
   - Observe users performing tasks; no expert knowledge required, just familiarity.
2. **Identifying Knowledge Representations**:
   - Determine what users need to know (e.g., task order, memorization) to complete a task, such as navigation or action sequences.
3. **Applying Focused Knowledge Elicitation Methods**:
   - Use techniques like "think-aloud" protocols to capture users' thought processes, including what influences their approach and changes in strategy.
4. **Analyzing and Verifying Data**:
   - Confirm the accuracy of collected data and interpretations.
5. **Formatting Results for Intended Application**:
   - Present results as models or flowcharts, with tasks represented in boxes.

*Result*: A flowchart-like representation of tasks and thought processes.

## Hierarchical Task Analysis

Hierarchical Task Analysis (HTA) breaks tasks into smaller, reusable components to identify available tools or design transferable elements across tasks and contexts. The process involves:

1. **Abstracting Unnecessary Details**: Focus on the appropriate level of abstraction.
2. **Modularizing Designs or Principles**: Create reusable components transferable between tasks or contexts.
3. **Organizing for Clarity**: Structure the analysis to enhance understanding and reasoning.

## Strengths and Weaknesses of Cognitive Task Analysis

### Strengths

1. **Emphasizes Mental Processes**: Unlike GOMS, CTA focuses on what happens in the user's mind (e.g., memory, attention).
2. **Formal Enough for Interface Design**: Results are structured and communicable for designing user interfaces.

### Weaknesses

1. **Time-Intensive**: Requires extensive data collection and systematic analysis.
2. **May Deemphasize Context**: Overlooks the role of external artifacts or environmental details.
3. **Ill-Suited for Novices**: Assumes some user familiarity, making it less effective for beginners.

## Other Task Analysis Methods

### Human Information Processor Models

- **KLM (Keystroke-Level Model)**: Analyzes efficiency via operator execution times.
- **TLM (Touch-Level Model)**: Similar to KLM but for touch-based interfaces.
- **MLP (Model Human Processor)**: A broader model of human processing.
- **CPM-GOMS**: Supports parallel task execution.
- **NGOMSL (Natural Language GOMS)**: Focuses on natural language and working memory.

### Cognitive Models

- **CDM (Critical Decision Model)**: Emphasizes critical decision points.
- **TKS (Task Knowledge Structures)**: Focuses on user knowledge.
- **CFM (Cognitive Function Model)**: Analyzes cognitive complexity.
- **Applied CTA** and **Skilled CTA**: Specialized CTA approaches.

## Important Videos

Videos 2, 5, 7, 8, 10, 11, and 13 are relevant for further understanding.

## Section Quizzes

### Design Challenge: Security System 1

*Morgan will disable the security system in two different ways. Outline her goals, outcomes, methods, and selection rules.*

|                 | Scenario 1              | Scenario 2              |
|-----------------|-------------------------|-------------------------|
| **Goals**       | Disable security system | Disable security system |
| **Outcomes**    | System disabled         | System disabled         |
| **Methods**     | Use keypad              | Use remote              |
| **Selection Rules** | Normal way          | Convenient way          |

### Reflections: Task Analysis

*Given behaviorism (emphasizing behavior as a product of stimuli and environment) and cognitivism (emphasizing internal thought processes), how much attention should you devote to observable goals, operators, and methods versus internal thought processes like cognition, learning, and memory?*

A 50-50 split between behaviorism and cognitivism is ideal. Understanding observable actions (goals, operators, methods) provides insights into user behavior, while exploring internal thought processes (cognition, learning, memory) ensures a well-rounded product design that accounts for both external interactions and mental models.

### Design Challenge: Security System 2

*Build a model of the sequence of thoughts in Morgan's head when disabling the security system in two ways, focusing on what she needs to remember at each step.*

| **Thoughts** | **Scenario 1**                            | **Scenario 2**                             |
|--------------|-------------------------------------------|--------------------------------------------|
| 1            | Open door                                 | Open door                                  |
| 2            | Turn left                                 | Take out remote                            |
| 3            | Enter code on security keypad             | Press button to disable security system    |
| 4            | Press enter to disable security system    |                                            |
# Lesson 11: HCI Context Models

In this lesson, we explore four models and theories surrounding Human-Computer Interaction (HCI) that emphasize context:

1. **Distributed Cognition**
2. **Social Cognition**
3. **Situated Action**
4. **Activity Theory**

## Distributed Cognition

Distributed cognition posits that cognitive processes extend beyond the individual mind, incorporating external artifacts. For example, adding large numbers in your head is more difficult than using pen and paper, where the paper serves as an extension of the cognitive process. Artifacts do not make the user smarter but distribute cognition across objects and tools.

### How a Cockpit Remembers Its Speeds

Given the dynamic nature of flight, how does a cockpit remember its speeds? The cockpit, as a system, comprises multiple cognitive components, each contributing to the memory of speeds:

1. **Long-term Memory**: A library of configurations (e.g., a booklet).
2. **Short-term Memory**: A specific configuration (e.g., one sheet).
3. **Working Memory**: Use of speed bugs on a dial.
4. **Deliberation**: Collaboration between the two pilots.

Each component serves as an individual cognitive element within the cockpit’s cognitive system.

### Distributed Cognition and Cognitive Load

Artifacts act as external memory, reducing cognitive load. For example, in driving, GPS and cruise control offload navigation and speed control tasks, mitigating cognitive overload. This allows users to focus on higher-level tasks.

### Distributed Cognition as a Lens

Distributed cognition provides a framework for approaching design problems by considering how artifacts and interfaces extend cognition. For instance, separating monitors can distribute cognitive tasks across multiple displays, enhancing efficiency.

## Transition from Distributed Cognition to Social Cognition

Distributed cognition focuses on extending the mind through artifacts and individuals. Social cognition builds on this by emphasizing how cognition is distributed across multiple individuals, enabling collaborative task completion.

## Social Cognition

Social cognition examines how social connections create systems that collectively accomplish tasks. It also explores the cognitive underpinnings of social interactions. For example, in the past, map reading during driving involved one person navigating while another drove, distributing cognitive tasks across individuals.

## Situated Action

Situated action emphasizes the context in which interactions occur, focusing on immediate, novel situational problems rather than long-term, enduring interactions. Key principles include:

1. **Contextual Interface Design**: Interfaces must be examined within the context of their use.
2. **Task Emergence**: Tasks arise from user interaction with the interface and are not predefined.
3. **User-Defined Tasks**: The task takes shape only when the user begins interacting.

### Situated Action and Memory

Memory is context-dependent. For example, people are more likely to remember a list of personal tasks embedded in a larger narrative than a list of tasks assigned by someone else.

## Activity Theory

Activity Theory is a comprehensive framework predating HCI, focusing on interactions within an activity. It generalizes the unit of analysis from tasks to activities, emphasizing the "why" behind user actions. Key contributions to HCI include:

1. **Generalizing Tasks to Activities**: Analysis focuses on the purpose of user actions, not just the actions themselves.
2. **Hierarchical Actions**: Low-level operations can be derived from higher-level actions, and user actions can move up and down this hierarchy due to learning or context.
3. **Dynamic Analysis**: Recognizes that activities evolve, influenced by user goals and environmental factors.

## Important Videos

Videos 2, 4, 5, 6, 10, 12, 13, and 15 are relevant for further understanding.

## Section Quizzes

### Exercise: Distributed Cognition

*Which of the following are playing cognitive roles in the system that is paying Morgan's bills?*

1. Morgan
# Lesson 12: Interfaces and Politics

In this lesson, we explore the intersection of interfaces and politics in Human-Computer Interaction (HCI), focusing on how technical artifacts embody authority or power, whether intentionally or unintentionally. We draw on Langdon Winner's question, "Do artifacts have politics?" to examine how technologies can shape societal change. The lesson covers two dimensions of politics, value-sensitive design, and the relationship between technology and society.

- **Politics**: The extent to which artifacts personify forms of authority or power, which can have positive or negative implications.

### Two Dimensions of Politics
1. **Designing for Change**: Intentionally creating interfaces to influence user behavior or societal outcomes.
2. **Anticipating Change from Designs**: Recognizing the unintended consequences that designs may have on society.

## Change: A Third Motivation

HCI traditionally pursues three goals:

1. **Help a User Do a Task**: Enhance task efficiency and usability.
2. **Understand How a User Does a Task**: Analyze user interactions to improve designs.
3. **Change the Way a User Does a Task**: Influence behavior or societal practices through design.

For example, car seatbelts prioritize safety (a change in behavior) over mere usability, illustrating how design can enforce societal values.

## Paper: Do Artifacts Have Politics?

Langdon Winner argues that technical devices carry political implications, shaping social order and power dynamics. Two types of political artifacts are identified:

1. **Inherently Political Technologies**:
   - **Nuclear Power**: Requires centralized, top-down control, aligning with authoritarian structures.
   - **Solar Power**: Supports distributed, decentralized systems, fostering egalitarian societies.
2. **Technical Arrangements as Forms of Order**:
   - Technologies can alter social structures based on context and purpose. For example, low bridges designed to restrict bus access to parks excluded poorer communities reliant on public transport, reinforcing social hierarchies.

## Change by Design

Interfaces can be deliberately designed to drive behavioral or societal change, with positive or negative outcomes:

- **Positive Examples**:
  - Facebook's *Like* button encourages positive social interactions and engagement, shaping societal trends.
- **Negative Examples**:
  - Low bridges restricting access to parks for poorer communities, preserving wealth-based social order.
  - Net neutrality debates highlight how access to technology can reinforce or challenge power structures.

The ability of interfaces to change behavior can be abused, embedding underlying political motivations in seemingly normal designs.

## Change by Happenstance

Technological changes can occur unintentionally, with both positive and negative consequences:

- **Positive Examples**:
  - The bicycle enabled women to travel independently, leading to societal changes like wardrobe reform and increased autonomy.
- **Negative Examples**:
  - Internet access, while democratizing information, can exacerbate inequalities due to existing infrastructure disparities.

These unintended effects highlight the need to anticipate the broader impact of designs.

## Value-Sensitive Design

Value-sensitive design (VSD) integrates human values into the design process in a principled and systematic manner, ensuring that interfaces align with ethical and societal priorities. For example, "privacy by design" embeds privacy as a core value in system architecture.

### Value-Sensitive Design and Information Systems

VSD involves three types of investigations:

1. **Conceptual Investigations**: Thought experiments to explore the role of values for stakeholders.
2. **Empirical Investigations**: Studying target users to understand how they perceive and prioritize values.
3. **Technical Investigations**: Analyzing how systems support or undermine specific values.

VSD is proactive, balancing usability with human values to create ethically sound designs.

### Value-Sensitive Design Across Cultures

Values vary across cultures, posing challenges for VSD:

- **Privacy vs. Free Speech**: Cultures valuing privacy (e.g., the EU's "right to be forgotten") may conflict with those prioritizing free speech due to censorship concerns.
- **Cultural Differences**: Google, designed without the "right to be forgotten," faced challenges in the EU, where this value is not universally shared.

Designers must navigate these differences to create inclusive systems.

### 5 Tips for Value-Sensitive Design

1. **Start Early**: Identify values at the outset of the design process and revisit them throughout.
2. **Know Your Users**: Understand user values and anticipate challenges in aligning designs with those values.
3. **Consider Direct and Indirect Stakeholders**: Account for both users and those affected by the system (e.g., non-users impacted by a bank’s UI).
4. **Brainstorm Interface Possibilities**: Explore how the interface might be used, including potential misuses (e.g., tracking hours leading to unjust terminations).
5. **Support vs. Prescribe Values**: Carefully choose whether to support existing user values or prescribe new ones, avoiding universal imposition of values.

## Reversing the Relationship

While technology shapes society, society also influences technology. For example:

- **User Demand**: Demand for a single platform to manage TV subscriptions drove the development of unified streaming services.
- **Societal Priorities**: The shift from fluorescent bulbs to energy-efficient alternatives was driven by electricity cost concerns, reflecting societal values around sustainability and cost-saving.

These dynamics highlight how societal needs can reshape technological development, sometimes preserving existing power structures (e.g., organizational influence in energy markets).

## Section Quizzes

### Design Challenge: Change by Design

*Design an app for Morgan that would encourage her to get up and move more frequently without explicitly telling her to do so.*

A social media app where users in the same city share pictures of local landmarks could encourage Morgan to explore her surroundings and take photos, promoting physical activity indirectly.

### Reflections: Interfaces and Politics

*Think of an instance where some technology you use was designed with political motivation in mind.*

Piazza’s interface prominently features its job search tool on the landing page, suggesting a deliberate push to influence users toward career-related activities, potentially aligning with corporate or economic interests.

## Important Videos

Videos 2, 4, 5, 7, 8, 11, 12, and 14 are relevant for further understanding.

# Lesson 13: HCI Design Principles

In this lesson, we tie together various threads of design principles in Human-Computer Interaction (HCI) by exploring three levels of interaction: Human as Processor, Predictor, and Participant. We also discuss practical UI design tips and the importance of understanding users to create effective interfaces.

## Zooming Out: Human as Processor

At the narrowest level, HCI focuses on the direct interaction between a person and an interface. This perspective is embodied by models like the **GOMS Model**, which analyzes user tasks in terms of goals, operators, methods, and selection rules, treating the human as an information processor.

## Zooming Out: Human as Predictor

At a broader level, HCI examines how users interact through an interface to accomplish tasks. This perspective considers the **gulf of execution** (the gap between a user’s intentions and the actions required by the interface) and the **gulf of evaluation** (the gap between the interface’s feedback and the user’s understanding of the outcome). Tools like **Cognitive Task Analysis** and **Hierarchical Task Analysis** help designers understand:

- Users’ mental models.
- Potential errors.
- Mappings between interface representations and underlying tasks.

Design principles at this level aim to align interfaces with users’ expectations and cognitive processes.

## Zooming Out: Human as Participant

At the highest level, HCI extends beyond the individual, interface, and task to consider the broader context of interaction. This perspective incorporates several theories and models:

- **Activity Theory**: Examines interactions within the context of activities, focusing on the "why" behind user actions and the hierarchical nature of tasks.
- **Distributed Cognition**: Analyzes how artifacts (e.g., tools, interfaces) combine to accomplish tasks by extending cognitive processes.
- **Situated Action**: Emphasizes the immediate, context-dependent nature of interactions, where tasks emerge from the user’s engagement with the environment.
- **Social Cognition**: Explores how social norms and relationships facilitate collaborative task completion.

Designers must also consider the intended and unintended positive and negative societal impacts of their designs, ensuring that interfaces align with broader ethical and social goals.

## 5 Tips: On-Screen UI Design

To create effective on-screen user interfaces, follow these principles:

1. **Use a Grid**: Ensure consistent alignment and structure for visual elements.
2. **Use Whitespace**: Enhance readability and reduce visual overload.
3. **Know Your Gestalt Principles**: Understand how users perceive and group visual elements (e.g., proximity, similarity) to create intuitive layouts.
4. **Reduce Clutter**: Leverage grids, whitespace, and Gestalt principles to simplify the interface.
5. **Design in Greyscale**: Focus on layout and contrast before adding color to avoid distraction.

## Only Half of the Picture

While design principles and frameworks provide a strong foundation for creating good interfaces, they represent only half of the equation. To design truly great user interfaces, designers must:

- Deeply understand their users’ needs, behaviors, and contexts.
- Recognize that they are not the user, avoiding assumptions based on their own experiences.

Empathy and user research are critical to bridging this gap

# Lesson 19: Evaluation in HCI

This lesson covers the evaluation of interface designs, focusing on gathering user feedback and assessing performance. The topics include:

1. **Evaluation**: Testing designs with users to collect feedback.
2. **Qualitative Evaluation**: Understanding user preferences (e.g., likes and dislikes).
3. **Empirical Evaluation**: Measuring performance metrics (e.g., task completion time).
4. **Predictive Evaluation**: Anticipating user feedback using principles and heuristics.

## Three Types of Evaluation

- **Qualitative Evaluation**: Emphasizes the totality of a phenomenon, capturing subjective user experiences (e.g., what users find easy or hard, likes/dislikes).
- **Empirical Evaluation**: Relies on numeric summaries or observations, often comparing designs to draw strong conclusions (typically conducted after qualitative evaluation with more participants).
- **Predictive Evaluation**: Uses systematic application of pre-established principles and heuristics to predict user interactions, ideal for rapid feedback when user testing is not feasible.

## Evaluation Terminology

- **Reliability**: Consistency of a measure in returning the same results for the same phenomenon.
- **Validity**: Whether a measure accurately reflects the underlying phenomenon (aligns results with reality).
- **Generalizability**: Ability of a measure’s results to predict phenomena beyond the specific context tested (applicability to broader audiences).
- **Precision**: Level of detail provided by a measure.

## 5 Tips: What to Evaluate

1. **Efficiency**: How quickly users (especially experts) complete tasks.
2. **Accuracy**: Number of errors users commit during tasks (expert performance).
3. **Learnability**: Time required for users to reach expertise.
4. **Memorability**: Users’ ability to recall how to use the interface over time.
5. **Satisfaction**: User enjoyment and cognitive load, accounting for social desirability bias (e.g., app download rates).

Key questions for evaluation planning:
- What data are you gathering?
- What are you evaluating?
- What approach will you use to evaluate?

## Evaluation Timeline

The evaluation process evolves over time, with different purposes, approaches, data types, and settings:

### Regarding Purpose
1. **Formative**: Aims to redesign and improve the interface during development.
2. **Summative**: Provides conclusive findings on the interface’s performance at the end.

### Regarding Approach
1. **Qualitative**: Focuses on understanding tasks and improving designs.
2. **Predictive**: Informs iterative revisions over time, similar to qualitative evaluation.
3. **Empirical**: Demonstrates or assesses measurable changes.

### Regarding Data
1. **Qualitative**: Always useful for interface improvement.
2. **Quantitative**: Requires rigorous evaluations but provides numerical insights.

### Regarding Setting
1. **Lab Testing**: Focuses exclusively on the interface in controlled conditions, ideal early on.
2. **Field Testing**: Evaluates the interface in real-world contexts.

## Evaluation Design

Steps to design an evaluation:

1. **Define the Task**: Specify the task (large or small) to be evaluated.
2. **Define Performance Measures**: Establish metrics (qualitative or quantitative) to avoid confirmation bias and ensure generalizability.
3. **Develop the Experiment**: Design surveys, interviews, or controlled tests, determining what to control or vary empirically.
4. **Recruit Participants**: Ensure ethical practices and participant awareness.
5. **Conduct the Experiment**: Execute the evaluation.
6. **Analyze the Data**: Interpret what the data reveals about performance measures, following up on unexpected findings.
7. **Summarize the Data**: Use results to inform ongoing design iterations.

## Qualitative Evaluation

Qualitative evaluation gathers subjective feedback

# Lesson 20: Agile Development in HCI

In this lesson, we explore how agile development methods enable quicker feedback cycles in Human-Computer Interaction (HCI). These methods emphasize early delivery, continuous improvement, and rapid feedback, transforming traditional HCI processes.

## The Demand for Rapid HCI

Historically, software development, distribution, and feedback were costly due to:

- Specialized development skills.
- Physical distribution methods.
- Difficulties in implementing fixes.
- The need for in-person user testing.

Modern advancements have reduced these barriers:

- **Cheap Development**: Accessible tools and platforms lower development costs.
- **Internet Distribution**: Free, instant updates via the internet.
- **Live Usage Data**: Real-time, abundant feedback from users.
- **Incentive to Iterate**: Rapid feedback encourages building and refining products quickly.

The challenge is to apply HCI principles (e.g., user-centered design, evaluation) within this rapid, agile development process.

## When to Go Agile

Deciding whether to adopt agile development depends on several factors:

|                   | Traditional         | Agile              |
|-------------------|---------------------|--------------------|
| **Criticality**   | High (e.g., healthcare, financial systems) | Low (e.g., games, social apps) |
| **Requirements**  | Rarely change       | Frequently change  |
| **Team Size**     | Large               | Small              |
| **Team Culture**  | Embraces order      | Embraces change    |

For example, a thermostat (stable requirements) suits traditional development, while a dynamic platform like Udacity (frequently changing requirements) benefits from agile methods.

## Towards a Framework for Integrating Agile Development and User-Centered Design (UCD)

Agile development and UCD share similarities but also have key differences, necessitating a framework for integration.

### Similarities Between UCD and Agile Development
- **Iterative Process**: Both rely on iterative cycles, building on empirical feedback. For example:
  - Agile’s Extreme Programming (XP) emphasizes feedback through refactoring [2:20].
  - UCD’s founding principle is iterative design.
- **User Focus**: Both prioritize user involvement:
  - In Scrum, users evaluate products monthly during sprint reviews, and the Product Owner manages requirements [16:54].
  - UCD emphasizes early and continual focus on users.
- **Team Coherence**: Both value team unity:
  - XP’s planning game fosters team collaboration [2:85].
  - UCD ensures the team keeps users in mind throughout development.

### Differences Between UCD and Agile Development
1. **Documentation**:
   - UCD advocates for design artifacts to support communication with developers.
   - Agile methods prioritize minimal documentation to accelerate development.
2. **Up-Front Investigation**:
   - UCD encourages deep user understanding before building.
   - Agile methods favor immediate coding over extensive pre-development research.

### Integration Framework
To integrate agile and UCD:
- Combine iterative feedback with user involvement.
- Balance minimal documentation with essential design artifacts.
- Conduct lightweight user research during sprints to align with agile’s rapid pace.

## Live Prototyping

Live prototyping tools, like Optimizely, allow rapid interface revisions using drag-and-drop interfaces. Benefits include:

- Quick iteration on small changes.
- Immediate user feedback on prototypes vs. final interfaces.
- High impact with minimal effort, ideal for agile environments.

## A/B Testing

A/B testing enables rapid comparison of two interface versions:

- Deploy version B to a small user group.
- Measure performance (e.g., engagement, task success).
- Roll out the better version to all users if results are positive.

This method supports real-world user testing within agile cycles.

## Agile HCI in the Design Life Cycle

Agile development does not replace the HCI design life cycle (e.g., need-finding, prototyping, evaluation) but accelerates it and adapts the types of prototypes and evaluations used. Key changes include:

- Faster iteration through design phases.
- Emphasis on lightweight prototypes (e.g., live prototyping).
- Rapid evaluation methods (e.g., A/B testing, usage data analysis).

The initial need-finding step remains critical to ensure user-centered design.

## 5 Tips: Mitigating Risk in HCI and Agile Development

1. **Start More Traditional**: Begin with traditional HCI methods (e.g., thorough need-finding) to establish a foundation, then transition to agile for iterative refinement.
2. **Focus on Small Changes**: Avoid large-scale changes to minimize

# Lesson 21: HCI Methods and Design Principles

In this lesson, we tie together various topics on HCI methods and design principles, using the case study of designing an audiobook app for exercisers to illustrate the iterative design process. We also explore how research methods integrate with design principles and examine different approaches to user-centered design.

## Designing Audiobooks for Exercisers

Creating an audiobook app for exercisers requires multiple iterations of the design cycle to reach a finished product. However, releasing the product does not mark the end of the design process. Once real users begin interacting with the app, the design cycle restarts, incorporating user feedback to refine and evolve the product. In essence, the design life cycle is continuous, adapting to the product’s growth and user needs over time.

## Research Methods Meet Design Principles

Design principles encapsulate insights and conclusions from past design cycles, enabling their application to new tasks and interfaces. These principles serve as transferable guidelines, informed by research methods such as user testing, task analysis, and evaluation, ensuring that new designs build on established knowledge.

## Approaches to User-Centered Design

User-centered design (UCD) prioritizes users’ needs and experiences throughout the design process. Different approaches to UCD include:

1. **Participatory Design**:
   - Involves all stakeholders, including users, as active members of the design team.
   - Ensures user perspectives shape the design but requires caution to avoid over-representing the participating users’ views, which may not reflect the broader user base.
2. **Action Research**:
   - Focuses on addressing an immediate problem while simultaneously researching it by attempting to solve it.
   - Combines practical problem-solving with knowledge generation.
3. **Design-Based Research**:
   - Similar to action research but can be conducted by external practitioners, not just those directly involved in the problem.
   - Commonly used in learning science research to iteratively design and study educational interventions.

## Important Videos

Videos 2, 3, 4, 6, and 8 are relevant for further understanding.