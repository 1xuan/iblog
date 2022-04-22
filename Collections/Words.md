# Some Words of Wisdom

> Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.  —Brian W. Kernighan

> "Copy and paste is a design error"    —David Parnas

> The age-old wisdom is dead-on: "Don’t document bad code—rewrite it".  —<<Code Complete>>

> Code as if whoever main- tains your program is a vio- lent psychopath who knows where you live  - Anonymous

> The first 90 percent of the code accounts for the first 90 percent of the development time. The remaining 10 percent of the code accounts for the other 90 percent of the development time. - Tom Cargill

> Experts agree that the best way to prepare for future requirements is not to write speculative code; it’s to make the currently required code as clear and straightforward as possible so that future programmers will know what it does and does not do and will make their changes accordingly.     —<<Code Complete>>

> More computing sins are committed in the name of efficiency (without necessarily achieving it) than for any other single reason— including blind stupidity. —W. A. Wulf

> We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.  Yet we should not pass up our opportunities in that critical 3%.   - Donald Knuth

If you haven’t spent at least a month working on the same program—working 16 hours a day, dreaming about it during the remaining 8 hours of restless sleep, working several nights straight through trying to eliminate that “one last bug” from the program—then you haven’t really written a complicated computer program. And you may not have the sense that there is something exhilarating about programming.  —Edward Yourdon


# <<Code Complete>> - Steve McConnell

### Chapter 25 Code-Tuning Strategies

> Some people look at the world through rose-colored glasses. Programmers like you and me tend to look at the world through code-colored glasses. We assume that the better we make the code, the more our clients and customers will like our software.

> The mere act of making goals explicit improves the likelihood that they’ll be
achieved. Programmers work to objectives when they know what they are; the
more explicit the objectives, the easier they are to work to. 

> The team who designed the ALGOL language—the granddaddy of most modern languages and one of the most influential languages ever—received the following advice: “The best is the enemy of the good.” Working toward perfection might prevent completion. Complete it first, and then perfect it. The part that needs to be perfect is usually small.

> In short, premature optimization’s primary drawback is its lack of perspective.

### Chapter 27 How Program Size Affects Construction 

> Larger-size projects demand organizational techniques that streamline communication or limit it in a sensible way.

> Productivity has a lot in common with software quality when it comes to project size.  At small sizes (2000 lines of code or smaller), the single biggest influence on productivity is the skill of the individual programmer (Jones 1998). As project size increases, team size and organization become greater influences on productivity. -section 27.4 Effect of Project Size on Productivity

> Writing 2K lines of code doesn’t take as long as creating a whole program that contains 2K lines of code. If you don’t consider the time it takes to do nonconstruction activities, development will take 50 percent more time than you estimate. - 27.5 Effect of Project Size on Development Activities

> In social settings, the more formal the event, the more uncomfortable your clothes have to be (high heels, neckties, and so on). In software development, the more formal the project, the more paper you have to generate to make sure you’ve done your homework. Capers Jones points out that a project of 1,000 lines of code will average about 7 percent of its effort on paperwork, whereas a 100,000-lines-of-code project will average about 26 percent of its effort on paperwork (Jones 1998). - 27.5 Effect of Project Size on Development Activities

> the more people’s brains you have to coordinate, the more formal documentation you need to coordinate them. - 27.5 Effect of Project Size on Development Activities

> “More” is not better, as far as methodologies are concerned. In their review of agile vs. plan-driven methodologies, Barry Boehm and Richard Turner caution that you’ll usually do better if you start your methods small and scale up for a large project than if you start with an all-inclusive method and pare it down for a small project (Boehm and Turner 2004). Some software pundits talk about “lightweight” and “heavyweight” methodologies, but in practice the key is to consider your project’s specific size and type and then find the methodology that’s “right-weight.” - 27.5 Effect of Project Size on Development Activities

> Scaling up a lightweight methodology tends to work better than scaling down a
heavyweight methodology.

### Chapter 28 Managing Construction

> For any project attribute, it’s possible to measure that attribute in a way that’s superior to not measuring it at all - 28.4

> In software development, nontechnical managers are common, as are managers who
have technical experience but who are 10 years behind the times. Technically competent, technically current managers are rare. If you work for one, do whatever you can to keep your job. It’s an unusual treat. - 28.6


### Chapter 31 Layout and Style

> In this case, the “clever” version carries an 11 percent speed penalty, which makes it look a lot less clever. The results vary from compiler to compiler, but in general they suggest that until you’ve measured performance gains, you’re better off striving for clarity and correctness first, performance second.


### Chapter 33: Personal Character

> The most important work in effective programming is thinking, and people tend not to look busy when they’re thinking. If I worked with a programmer who looked busy all the time, I’d assume that he was not a good programmer because he wasn’t using his most valuable tool, his brain.  - 33.7 Laziness



# <<Refactoring>>  second edition -Martin Fowler

My overall advice on performance with refactoring is: Most of the time you should ignore it.

When programming, follow the camping rule: Always leave the code base leahthier than when you found it. It will never be perfect, but it should be better.

The true test of good code is how easy it is to change it.

I am a very lazy programmer. One of my forms of laziness is that I never remember things about the code I write. Indeed, I deliberately try not remember anything I can look up, because I'm afraid my brain will get full. I make a point of trying to put everything I should remember into the code so I don't have to remember it.

It reminds me of a statement Kent Beck often makes about himself: "I'm not a great programmer; I'm just a good programmer with great habits".


