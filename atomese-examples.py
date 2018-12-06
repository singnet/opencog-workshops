from opencog.utilities import initialize_opencog
from opencog.atomspace import AtomSpace, types
from opencog.type_constructors import *
from opencog.bindlink import bindlink
from opencog.bindlink import execute_atom


# new atomspace
atomspace = AtomSpace()

# add concept node
atomspace.add_node(types.ConceptNode, "small")
# set default atomspace to add atoms to
initialize_opencog(atomspace)
# add ConceptNode
ConceptNode("size")

# every Atom(nodes or links) has incoming and outgoing sets
print('ConceptNode("size").incoming:')
print(ConceptNode("size").incoming)

link = InheritanceLink(ConceptNode("small"), ConceptNode("size"))
print("create link {0}\n".format(link))
print("every Atom has default tv:")
print(link.tv)

print('setting new TruthValue')
link.tv = TruthValue(0.9, 0.9)

print(link)
print('outgoing set of the link:')
print(link.out)


print('\n incoming set of ConceptNode("size")')
print(ConceptNode("size").incoming)


# bindlink
# Bindlink structure
# 1. VariableList - optional
# 2. Conditional expression
# 3. Rewrite term

condition = InheritanceLink(VariableNode("X"), VariableNode("Y"))
bindlink1 = BindLink(condition, condition)

print("running bindlink")
print(bindlink(atomspace, bindlink1))


# ExecutionOutputLink
# ExecutionOutputLink structure
# 1. GroundedSchemaNode
# 2. ListLink of arguments

def add_node():
    return ConceptNode("Test")

exec1 = ExecutionOutputLink(
         GroundedSchemaNode("py: add_node"),
         ListLink())


print("running ExecutionOutputLink")
print(execute_atom(atomspace, exec1))

print("nested ExectutionOutputLinks")

def add_link(node):
    ev = EvaluationLink(
           PredicateNode("ok"),
           node)
    ev.tv = TruthValue(0.1, 0.8)
    return ev

exec2 = ExecutionOutputLink(
           GroundedSchemaNode("py: add_link"),
           ListLink(
             ExecutionOutputLink(
                 GroundedSchemaNode("py: add_node"),
                 ListLink()))
        )

print(execute_atom(atomspace, exec2))

