from opencog.utilities import initialize_opencog
from opencog.atomspace import AtomSpace, types
from opencog.type_constructors import *
from opencog.bindlink import bindlink
from opencog.bindlink import execute_atom





# knowledge base
# concepts
InheritanceLink(ConceptNode("small"), ConceptNode("size"))
InheritanceLink(ConceptNode("big"), ConceptNode("size"))
InheritanceLink(ConceptNode("green"), ConceptNode("color"))
InheritanceLink(ConceptNode("red"), ConceptNode("color"))
InheritanceLink(ConceptNode("black"), ConceptNode("color"))
# items
InheritanceLink(ConceptNode("item-0"), ConceptNode("small")).tv = TruthValue(0.4, 0.9)
InheritanceLink(ConceptNode("item-0"), ConceptNode("green")).tv = TruthValue(0.3, 0.9)
InheritanceLink(ConceptNode("item-2"), ConceptNode("big")).tv = TruthValue(0.4, 0.9)
InheritanceLink(ConceptNode("item-2"), ConceptNode("red")).tv = TruthValue(0.4, 0.9)
InheritanceLink(ConceptNode("item-1"), ConceptNode("red")).tv = TruthValue(0.2, 0.9)
InheritanceLink(ConceptNode("item-1"), ConceptNode("small")).tv = TruthValue(0.8, 0.9)
InheritanceLink(ConceptNode("item-3"), ConceptNode("black")).tv = TruthValue(0.14, 0.9)
InheritanceLink(ConceptNode("item-3"), ConceptNode("small")).tv = TruthValue(0.38, 0.9)



def apply_threshold(atom, num_node):
inh = InheritanceLink(VariableNode("X"), VariableLink("Y"))
eval_threshold = EvaluationLink(
                    GroundedPredicateNode("py: apply_threshold"),
                    ListLink(inh))
condition = AndLink(
