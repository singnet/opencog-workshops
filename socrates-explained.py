from opencog.bindlink import execute_atom, evaluate_atom
from opencog.scheme_wrapper import scheme_eval, scheme_eval_h
from opencog.atomspace import TruthValue
from opencog.backwardchainer import BackwardChainer
from opencog.type_constructors import *
from opencog.utilities import initialize_opencog
from opencog.scheme_wrapper import load_scm
from opencog.bindlink import bindlink
import opencog.logger


atomspace = AtomSpace()
initialize_opencog(atomspace)
scheme_eval(atomspace, '(use-modules (opencog))')
scheme_eval(atomspace, '(use-modules (opencog exec))')
scheme_eval(atomspace, '(use-modules (opencog query))')
scheme_eval(atomspace, '(use-modules (opencog rule-engine))')
scheme_eval(atomspace, '(add-to-load-path "/home/noskill/projects/opencog/opencog/pln")')
scheme_eval(atomspace, ('(load-from-path "/home/noskill/projects/opencog/opencog/pln/pln-config.scm")'))


var_a = VariableNode("$A")
var_b = VariableNode("$B")
var_c = VariableNode("$C")
var_list = VariableList(VariableNode("$A"), VariableNode("$B"), VariableNode("$C"))
BA = InheritanceLink(var_b, var_a)
CB = InheritanceLink(var_c, var_b)
CA = InheritanceLink(var_c, var_a)
condition = AndLink(BA, CB, NotLink(IdenticalLink(var_a, var_c)))
rewrite = ExecutionOutputLink(GroundedSchemaNode("scm: deduction-formula"),
                              ListLink(CA, CB, BA))

deduction_link = BindLink(var_list, condition, rewrite)

InheritanceLink(ConceptNode("Socrates"), ConceptNode("man")).tv = TruthValue(0.97, 0.92)
InheritanceLink(ConceptNode("man"), ConceptNode("mortal")).tv = TruthValue(0.98, 0.94)

print(bindlink(atomspace, deduction_link))

