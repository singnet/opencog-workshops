from opencog.bindlink import execute_atom, evaluate_atom
from opencog.scheme_wrapper import scheme_eval, scheme_eval_h
from opencog.atomspace import TruthValue
from opencog.backwardchainer import BackwardChainer
from opencog.type_constructors import *
from opencog.utilities import initialize_opencog
from opencog.scheme_wrapper import load_scm
import opencog.logger


global_storage = dict()

atomspace = AtomSpace()
initialize_opencog(atomspace)
scheme_eval(atomspace, '(use-modules (opencog))')
scheme_eval(atomspace, '(use-modules (opencog exec))')
scheme_eval(atomspace, '(use-modules (opencog query))')
scheme_eval(atomspace, '(use-modules (opencog rule-engine))')
scheme_eval(atomspace, '(add-to-load-path "/home/noskill/projects/opencog/opencog/pln")')
scheme_eval(atomspace, ('(load-from-path "/home/noskill/projects/opencog/opencog/pln/pln-config.scm")'))
InheritanceLink(ConceptNode("Socrates"), ConceptNode("man")).tv = TruthValue(0.97, 0.92)
InheritanceLink(ConceptNode("man"), ConceptNode("mortal")).tv = TruthValue(0.98, 0.94)
rbs = ConceptNode("PLN")
request = InheritanceLink(ConceptNode("Socrates"), ConceptNode("mortal"))
trace_atomspace = AtomSpace()
chainer = BackwardChainer(atomspace, rbs, request, trace_as=trace_atomspace)
chainer.do_chain()
traces = chainer.get_inference_trees()
print(chainer.get_results())

