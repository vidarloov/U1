def calculate_monthly_payment(principal, annual_rate, years):
    r = annual_rate / 12 / 100
    n = years * 12
    A = (principal * r) / (1 - (1 + r) ** -n)
    
    return A

principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")