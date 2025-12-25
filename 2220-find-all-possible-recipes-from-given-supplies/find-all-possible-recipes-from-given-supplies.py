class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        can_cook = {s: True for s in supplies}
        index_recipe = {r:i for i, r in enumerate(recipes)}
        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            if r not in index_recipe:
                return False
            can_cook[r] = False
            for i in ingredients[index_recipe[r]]:
                if not dfs(i):
                    return False
            can_cook[r] = True
            return can_cook[r]

        Can_be_cooked = []
        for r in recipes:
            if dfs(r):
                Can_be_cooked.append(r)
        return Can_be_cooked