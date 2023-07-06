# All About Sets
Sets are a bit different from queues or stacks. For example, stacks have a first in, last out principle, and queues have a first in, first out principle. In sets, however, order doesn't matter at all. Putting data anywhere inside of a set really won't have any effect on whether or not you're able to "pop" or "append" an item within a set.

![Collection](images/collection.jpg)

I like to think of sets as a collection of objects, like unique knick-knacks you bought as souveniers from places you've travelled, or baseball cards you've collected over the years. It's a collection of unique items that you're able to place and take off of a shelf. 

Another key difference is that sets don't allow any duplicates within the item list. The big O notation within a set is usually O(1) when you impliment a technique known as __hashing.__ Hashing allows the ability to add, remove, and test to see if an item is inside of a set, so it's very useful when we work with these sort of data structures. 