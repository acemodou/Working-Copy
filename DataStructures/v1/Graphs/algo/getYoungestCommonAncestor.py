def simple_assert(a, b):
    assert a == b, f"{a}!{b}"

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backTrackAnscestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backTrackAnscestralTree(descendantTwo, descendantOne, depthTwo - depthOne)

def getDescendantDepth(descendant, topAncestor):
    depth = 0 
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth 

def backTrackAnscestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0: 
        diff -= 1
        lowerDescendant = lowerDescendant.ancestor 
    
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor 
        higherDescendant = higherDescendant.ancestor 
    return lowerDescendant 

class AncestralTree(AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


trees = new_trees()
trees["A"].addDescendants(trees["B"], trees["C"])
trees["B"].addDescendants(trees["D"], trees["E"])
trees["D"].addDescendants(trees["H"], trees["I"])
trees["C"].addDescendants(trees["F"], trees["G"])

yca = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
simple_assert(yca, trees["B"])