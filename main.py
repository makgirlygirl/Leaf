import textwrap
import warnings
warnings.filterwarnings(action='ignore')

from app.mcq_generation import MCQGenerator

def show_result(generated: str, answer: str, context:str, original_question: str = ''):
    print('show_result')
    
    print('Context:')

    for wrap in textwrap.wrap(context, width=120):
        print(wrap)
    print()

    print('Question:')
    print(generated)

    print('Answer:')
    print(answer)
    print('-----------------------------')


MCQ_Generator = MCQGenerator(True)

context = '''The koala or, inaccurately, koala bear[a] (Phascolarctos cinereus), is an arboreal herbivorous marsupial native to Australia. It is the only extant representative of the family Phascolarctidae and its closest living relatives are the wombats, which are members of the family Vombatidae. The koala is found in coastal areas of the mainland's eastern and southern regions, inhabiting Queensland, New South Wales, Victoria, and South Australia. It is easily recognisable by its stout, tailless body and large head with round, fluffy ears and large, spoon-shaped nose. The koala has a body length of 60–85 cm (24–33 in) and weighs 4–15 kg (9–33 lb). Fur colour ranges from silver grey to chocolate brown. Koalas from the northern populations are typically smaller and lighter in colour than their counterparts further south. These populations possibly are separate subspecies, but this is disputed.'''

context_oxygen = '''Oxygen is the chemical element with the symbol O and atomic number 8. It is a member of the chalcogen group in the periodic table, a highly reactive nonmetal, and an oxidizing agent that readily forms oxides with most elements as well as with other compounds. Oxygen is Earth's most abundant element, and after hydrogen and helium, it is the third-most abundant element in the universe. At standard temperature and pressure, two atoms of the element bind to form dioxygen, a colorless and odorless diatomic gas with the formula O
2. Diatomic oxygen gas currently constitutes 20.95% of the Earth's atmosphere, though this has changed considerably over long periods of time. Oxygen makes up almost half of the Earth's crust in the form of oxides.[3]

Dioxygen provides the energy released in combustion[4] and aerobic cellular respiration,[5] and many major classes of organic molecules in living organisms contain oxygen atoms, such as proteins, nucleic acids, carbohydrates, and fats, as do the major constituent inorganic compounds of animal shells, teeth, and bone. Most of the mass of living organisms is oxygen as a component of water, the major constituent of lifeforms. Oxygen is continuously replenished in Earth's atmosphere by photosynthesis, which uses the energy of sunlight to produce oxygen from water and carbon dioxide. Oxygen is too chemically reactive to remain a free element in air without being continuously replenished by the photosynthetic action of living organisms. Another form (allotrope) of oxygen, ozone (O
3), strongly absorbs ultraviolet UVB radiation and the high-altitude ozone layer helps protect the biosphere from ultraviolet radiation. However, ozone present at the surface is a byproduct of smog and thus a pollutant.

Oxygen was isolated by Michael Sendivogius before 1604, but it is commonly believed that the element was discovered independently by Carl Wilhelm Scheele, in Uppsala, in 1773 or earlier, and Joseph Priestley in Wiltshire, in 1774. Priority is often given for Priestley because his work was published first. Priestley, however, called oxygen "dephlogisticated air", and did not recognize it as a chemical element. The name oxygen was coined in 1777 by Antoine Lavoisier, who first recognized oxygen as a chemical element and correctly characterized the role it plays in combustion.

Common uses of oxygen include production of steel, plastics and textiles, brazing, welding and cutting of steels and other metals, rocket propellant, oxygen therapy, and life support systems in aircraft, submarines, spaceflight and diving.'''

eng_test1='''Scientists use paradigms rather than believing them. The use of a paradigm in research typically addresses related problems by employing shared concepts, symbolic expressions, experimental and mathematical tools and procedures, and even some of the same theoretical statements. Scientists need only understand how to use these various elements in ways that others would accept. These elements of shared practice thus need not presuppose any comparable unity in scientists’ beliefs about what they are doing when they use them. Indeed, one role of a paradigm is to enable scientists to work successfully without having to provide a detailed account of what they are doing or what they believe about it. Thomas Kuhn noted that scientists “can agree in their identification of a paradigm without agreeing on, or even attempting to produce, a full interpretation or rationalization of it. Lack of a standard interpretation or of an agreed reduction to rules will not prevent a paradigm from guiding research.”'''
eng_test2='''Philip Kitcher and Wesley Salmon have suggested that there are two possible alternatives among philosophical theories of explanation. One is the view that scientific explanation consists in the unification of broad bodies of phenomena under a minimal number of generalizations. According to this view, the (or perhaps, a) goal of science is to construct an economical framework of laws or generalizations that are capable of subsuming all observable phenomena. Scientific explanations organize and systematize our knowledge of the empirical world; the more economical the systematization, the deeper our understanding of what is explained. The other view is the causal/mechanical approach. According to it, a scientific explanation of a phenomenon consists of uncovering the mechanisms that produced the phenomenon of interest. This view sees the explanation of individual events as primary, with the explanation of generalizations flowing from them. That is, the explanation of scientific generalizations comes from the causal mechanisms that produce the regularities. 
'''
# MCQ_Generator.generate_mcq_questions(context_oxygen, 10)
MCQ_Generator.generate_mcq_questions(eng_test2, 10)

