class TrieNode:
   def __init__(self):
      self.children = {}
      self.endOfString = False

class Trie:
   def __init__(self):
      self.root = TrieNode()

   def insert(self,word):
      current = self.root
      for i in word:
         node = self.root.children.get(i)
         if(node == None):
            node = TrieNode()
            current.children.update( { i: node } )
         print(current.children)
         current = node        
      current.endOfString = True
      print("Inserted")

   def search(self,word):
      current = self.root
      for i in word:
         node = current.children.get(i)
         if(node == None):
            print("Does not exist")
            return
         current = node
      if(current.endOfString == True):
         print("Exists")
         return
      print("Does not exists")

   def delete(self,root,word,index):
      ch = word[index]
      currentNode = root.children.get(ch)
      tobeDeleted = False

      if(len(currentNode.children) > 1):
         self.delete(currentNode,word,index+1)
         return False
      
      if(index == len(word) - 1):
         if(len(currentNode.childern >= 1)):
            currentNode.endOfString = False
            return False
         else:
            root.children.pop(ch)
            return True
      
      if(currentNode.endOfString == True): 
         #if some other word is prefix of the 'word'
         self.delete(currentNode,word,index+1)
         return False
      
      tobeDeleted = self.delete(currentNode,word,index+1)
      if(tobeDeleted == True):
         root.children.pop(ch)
         return True
      else:
         return False

trie = Trie()
trie.insert("App")
trie.insert("Apps")
# trie.search("Appi")
trie.delete(trie,"App",0)
trie.search("App")