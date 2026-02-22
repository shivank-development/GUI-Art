from ete3 import Tree, TreeStyle

# Newick format tree
t = Tree("(Human,(Chimp,Mouse));")

# Tree style
ts = TreeStyle()
ts.show_leaf_name = True

# Show tree
t.show(tree_style=ts)
