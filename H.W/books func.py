def book(title):
    print(f"book's name is {title}")

def book_price(price):
    print(f"the book price is :{price}$")

def page_book(total_pages,selected_page):
    leftToRead=total_pages-selected_page
    print(leftToRead)


def main():
    num=int(input("enter the how many boos are desired"))
    sum=0
    for i in range(num):
        title=input("enter title book here:")
        price=int(input("enter the price desired"))
        totalPages=int(input(f"how many pages {title} have"))
        selectedPage=int(input(f"which page in {title} did you read"))
        book(title)
        book_price(price)
        page_book(totalPages,selectedPage)
        sum=sum+price
        print("")
    print(f"for the price of {num} books are {sum}")
main()