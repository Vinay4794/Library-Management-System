#----------------------------------------Library Management System-----------------------------------------------------------------

# Function for Book Information
def book_info(a):
    if(a == 1):
     print("-------------------------------------------")
     print("NAME: Pride and Prejudice ")
     print("AUTHOR: Jane Austen ")
     print("YEAR OF PUBLISHING: 1813 ")
     print("PRICE: $199 ")
     print("DESCRIPTION: A novel of manners, it follows the character development of Elizabeth Bennet, the protagonist of the book, who learns about the repercussions of hasty judgments and comes to appreciate the difference between superficial goodness and actual goodness.")
    elif(a == 2):
     print("-------------------------------------------") 
     print("NAME: The Great Gatsby")
     print("AUTHOR:  F. Scott Fitzgerald")
     print("YEAR OF PUBLISHING: 1925")
     print("PRICE: $299 ")
     print("DESCRIPTION: The novel was inspired by a youthful romance Fitzgerald had with socialite Ginevra King and the riotous parties he attended on Long Island's North Shore in 1922. Following a move to the French Riviera, Fitzgerald completed a rough draft of the novel in 1924. He submitted it to editor Maxwell Perkins, who persuaded Fitzgerald to revise the work over the following winter. After making revisions, Fitzgerald was satisfied with the text but remained ambivalent about the book's title and considered several alternatives. Painter Francis Cugat's dust jacket art, named Celestial Eyes, greatly impressed Fitzgerald, and he incorporated its imagery into the novel.")
    elif(a==3):
     print("-------------------------------------------")
     print("NAME:To Kill a Mockingbird")
     print("AUTHOR: Harper Lee")
     print("YEAR OF PUBLISHING: 1960")
     print("PRICE: $349")
     print("DESCRIPTION: The story, told by Jean Louise Finch, takes place during three years (1933–35) of the Great Depression in the fictional town of Maycomb, Alabama, the seat of Maycomb County. Scout, who is six years old at the beginning of the book, lives with her older brother Jeremy, nicknamed Jem, and their widowed father Atticus, a middle-aged lawyer. They also have a black cook, Calpurnia, who has been with the family for many years and helps Atticus raise the two children.")  
    elif(a==4):
     print("-------------------------------------------")
     print("NAME: Moby-Dick")
     print("AUTHOR: Herman Melville")
     print("YEAR OF PUBLISHING:  1851")
     print("PRICE: $149")
     print("DESCRIPTION: Melville began writing Moby-Dick in February 1850 and finished 18 months later, a year after he had anticipated. Melville drew on his experience as a common sailor from 1841 to 1844, including on whalers, and on wide reading in whaling literature. The white whale is modeled on a notoriously hard-to-catch albino whale Mocha Dick, and the book's ending is based on the sinking of the whaleship Essex in 1820. The detailed and realistic descriptions of sailing, whale hunting and of extracting whale oil, as well as life aboard ship among a culturally diverse crew, are mixed with exploration of class and social status, good and evil, and the existence of God.")
    elif(a==5):
     print("-------------------------------------------")
     print("NAME: The Lord of the Rings")
     print("AUTHOR: John Ronald Reuel Tolkien")
     print("YEAR OF PUBLISHING: 1955")
     print("PRICE: $439")
     print("DESCRIPTION: The title refers to the story's main antagonist,[b] the Dark Lord Sauron, who in an earlier age created the One Ring, allowing him to rule the other Rings of Power given to men, dwarves, and elves, in his campaign to conquer all of Middle-earth. From homely beginnings in the Shire, a hobbit land reminiscent of the English countryside, the story ranges across Middle-earth, following the quest to destroy the One Ring, seen mainly through the eyes of the hobbits Frodo, Sam, Merry, and Pippin. Aiding the hobbits are the wizard Gandalf, the men Aragorn and Boromir, the elf Legolas, and the dwarf Gimli, who unite as the Company of the Ring in order to rally the Free Peoples of Middle-earth against Sauron's armies and give Frodo a chance to destroy the One Ring in the fires of Mount Doom.")
    else:
     print("-------------------------------------------")
     print("Oops... you have entered wrong input.")

# Main function for choosing the number 
def main():
    print("Press 1 for Book 101 Information\nPress 2 for Book 102 Information\nPress 3 for Book 103 Information\nPress 4 for Book 104 Information\nPress 5 for Book 105 Information")
    choise = int(input("Enter your choice :"))
    book_info(choise)
    print("-------------------------------------------")   
    print("Do you want to continue.......")
    c = int(input("Press 1 to continue or 0 to exit: "))
    print("-------------------------------------------")
    if(c == 0):
      print("Thanq for visiting my Library")
    elif(c == 1):
      main()
    else:
      print("Sorry You have entered wrong input value\nThanq")  
      
print("--------Library Management System--------\n")    
main()

    



































  
