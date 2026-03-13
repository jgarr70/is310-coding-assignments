from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Lip Product Reviews!", style="bold magenta")
table.add_column("Brand", style="dark_slate_gray1"  , no_wrap=True)
table.add_column("Name", style="orange1" , no_wrap=False)
table.add_column("Rating")
table.add_column("Comments", style="medium_purple1")
table.add_row("Eadem", "Le Chouchou", ":star::star::star::star::star:", "Super moisturizing!")
table.add_row("Cocokind", "Ceramide Lip Blur Balm", ":star::star::star:", "Not sticky")
table.add_row("OLEHENRIKSEN ", "Pout Preserve Hydrating Peptide Lip Treatment", ":star::star::star::star::star:", "Very long-lasting!")


console.print(table)

while True:
    console.print("\n[bold magenta]Do you want to add your own lip product review? (yes/no)[/bold magenta]")
    response = input().strip().lower()
    if response == "yes":
        brand = input("Enter the brand of the lip product: ")
        lippie = input("Enter the name of the lip product: ")
        rating = input("Enter the number of stars (1-5): ")
        while not rating.isdigit() or not 1 <= int(rating) <= 5:
            console.print("\n[bold red]Invalid rating. Please enter a number between 1 and 5.[/bold red]")
            rating = input("Enter the number of stars (1-5): ")
        comment = input("Enter your comments: ")
        console.print(f"\n[bold cyan]You entered: {brand}, {lippie}, {rating} stars, {comment}[/bold cyan]")
        table.add_row(brand, lippie, ":star:"*int(rating), comment)
        console.print(table)
    elif response == "no":
        console.print("\n[bold cyan]No problem! Enjoy the table![/bold cyan]")
        exit()
    else:
        console.print("\n[bold red]Invalid input. Please enter 'yes' or 'no'.[/bold red]")
    
