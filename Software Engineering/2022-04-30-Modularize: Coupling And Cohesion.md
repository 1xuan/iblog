# Modularize: Coupling And Cohesion

## Introducing

Over time, programmer more prefer to split system into multiple subsystems. Because they are aware: the more relevant parts of a piece of code, the more difficult to make modifications and make it correct. We can easily get a feel from experience: it is somewhat overwhelming when sevaral tasks(or problems) arise simultaneously, even more if it is parallel. We can't put our attention on varying things at the same time, it's more like a trick(imagine juggle 3 balls or more). As human beings, we are good at focusing on one thing, or say that [we can only focusing on one thing at the same time](https://www.youtube.com/watch?v=XmvSxppayTI). So the independence of modules become an important topic in software design.

There is a term, coupling, which is developed by Larry Constantine in the late 1960s as part of a structured design, to refer to the dependence **between modules**. From my perspective, a lot of people get it wrong, they just chop system into small pieces, that's all. The understanding of coupling is wrong, it oversimplified the concept, so that, in fact, not only is there more bugs, but also does developing become more inefficient.

> ... Successful design is based on a principle known since the days of Julius Caesar: Divide and conquer.
>
> Specifically, we suggest that the cost of implementing a computer system will be minimized when the parts of the problem are
>
> - manageably small
> - solvable separately
>
> ...
> 
> Of course, many designers have made attempts to "Chop" a system into manageably small pieces; unfortunately, they have often found that implementation time increased rather than decreased. The key frequently lies in the second part of our stipulation above: The parts of the original problem must be solvable separately. In many computer systems, we find that this is not so: In order to implement part A of the solution to the problem, we have to know something about part B ... and in order to solve part B, we have to know something about part C.
> 
> ... we can argue that the cost of maintenance is minimized when parts of the system are
>
> - easily related to the application
> - manageably small
> - correctable separately
>
> <pre>                            - &lt;&lt;Structured Design&gt;&gt; Larry Constantine </pre>

As often said: Do one thing at one time, we need to do only one thing in one module. Now, how to define the "one" is the most important part.

> By partitioning we mean the division of the problem into smaller subproblems, so that each subproblem will eventually correspond to a piece of the system. The questions are: Where and how should we divide the problem? Which aspects of the problem belong in the same part of the system, and which aspects belong in different parts?  Structured design answers these questions with two basic principles:
> 
> • Highly interrelated parts of the problem should be in the same piece of the system, i.e., things that belong together should go together.
> • Unrelated parts of the problem should reside in unrelated pieces of the system. That is, things that have nothing to do with one another don't belong together.
>
> <pre>                            - &lt;&lt;Structured Design&gt;&gt; Larry Constantine </pre>

Even though we aim to lower the coupling, however, **as long as any module belongs to system, coupling to the system must exist in some form, more or less**. 

Cohesion is contrast with coupling, refers to degree to which **the elements inside a module** belong together. Namely, **cohesion indicates the degree of dependence between intramodule elements, and coupling otherwise is degree of dependence between intermodule elements**. Usually, high cohesion indicates loose coupling, and vice versa. This means: the one of targets of system design is to achieve the highest cohesion. Usually speaking, paying attention on cohesion instead of coupling is more directly, intuitively, and easier. It narrows down what you have to focus on.


> Clearly, cohesion and coupling are interrelated. The greater the cohesion of individual modules in the system, the lower the coupling between modules will be. In actual practice, these two measures are correlated; that is, on the average, as one increases, the other decreases; but the correlation is not perfect. Maximizing the sum of module cohesion over all modules in a system should closely approximate the results one would obtain in trying to minimize coupling. However, it turns out to be easier both mathematically and practically to focus on cohesion.
>
> <pre>                            - &lt;&lt;Structured Design&gt;&gt; Larry Constantine </pre>

If modules are highly cohesive separately.

















P7:
Structured design is the art of designing the components of a system and the interrelationship between those components in the best possible way.

P16:
Of course, many designers have made attempts to 44 Chop" a system into manageably small pieces; unfortunately, they have often found that implementation time increased rather than decreased. The key frequently lies in the second part of our stipulation above: The parts of the original problem must be solvable separately. In many computer systems, we find that this is not so: In order to in)Plement part A of the solution to the problem, we have to know something about part B ... and in order to solve part B, we have to know something about part C.

P17:

In a similar fashion, we can argue that the cost of maintenance is minimized when parts of the system are:
    • easily related to the application
    • manageably small
    • correctable separately

Thus, when the user calls on the telephone to complain that the third line of the XYZ report is wrong, it may not immediately be clear which part of the system is responsible for producing the third line of the XYZ report. Indeed, it may turn out that several obscure parts of the system are involved in producing the third tine of the XYZ report. The larger the system, and the more subtle the bugs, the more critical it is that maintenance personnel be able to relate parts of the system to parts of the user's application.


By partitioning we mean the division of the problem into smaller subproblems, so that each subproblem will eventually correspond to a piece of the system. The questions are: Where and how should we divide the problem? Which aspects of the problem belong in the same part of the system, and which aspects belong in different parts?  Structured design answers these questions with two basic principles:

• Highly interrelated parts of the problem should be in the same piece of the system, i.e., things that belong together should go together.
• Unrelated parts of the problem should reside in unrelated pieces of the system. That is, things that have nothing to do with one another don't belong together.


P29:
Such interrelationships, though important to the programmer doing the detailed coding (e.g., HJeez, where are all the MOVE CORRESPONDAING statements in this program - it turns out, the compiler generates incorrect object code for them!"), can be ignored, for they do not really exist in the program. The associations are mental rather than physical.


In terms of writing, understanding, and modifying, a contiguous linear block of
code does not behave like many small pieces, but rather like one big, tightly cemented piece.The term monolithic refers to any system or portion of a system which consists of pieces so highly interrelated that they behave like a single piece.


P66:
Another possible contributor to complexity is the Hspann of data elements - i.e., the number of program statements during which the status and value of a data element must be remembered by the programmer in order to comprehend what the module is doing~ thus, a module is made more complex if a data element is loaded into an accumulator in the second instruction, and the data element then is not used until the 147th instruction.


All of these measures recognize that the human-perceived complexity of program
statements varies, influencing the apparent size of a module. Three factors, implicit in the above approaches, have been identified as affecting statement complexity:
• the amoum of information that must be understood correctly
• the accessibility of the information
• the structure of the information


P76:
The key question is: How much of one module must be known in order to understand another module? The more that we must know of module B in order to understand module A, the more closely connected A is to B.


P84:
The concept of binding time is an important one in program and systems design.  When the values of parameters within some piece of code are fixed late rather than early, they are more readily changed and the system becomes more adaptable to changing requirements.


P95:
Adapting the system's design to the problem structure (or "application structure") is an extremely important design philosophy; we generally find that problematically related processing elements translate into highly interconnected code. Even if this were not true, structures that tend to group together highly interrelated elements tend to be more effectively modular.


P96
Clearly, cohesion and coupling are interrelated. The greater the cohesion of individual modules in the system, the lower the coupling between modules will be. In actual practice, these two measures are correlated; that is, on the average, as one increases, the other decreases; but the correlation is not perfect. Maximizing the sum of module cohesion over all modules in a system should closely approximate the results one would obtain in trying to minimize coupling. However, it turns out to be easier both mathematically and practically to focus on cohesion.

