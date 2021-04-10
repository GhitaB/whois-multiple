import whois

with open("list-of-domains.txt") as file_in:
    for item in file_in:
        line = item.rstrip()
        domain_name = line
        try:
            domain_info = whois.query(domain_name)
            domain_expiration = domain_info.expiration_date
        except whois.exceptions.UnknownTld:
            domain_expiration = "error: Unknown TLD"

        print("{} - {}".format(domain_name, domain_expiration))

        file_out = open("output.csv", "a")
        file_out.write("{},{}\n".format(domain_name, domain_expiration))
        file_out.close()

# print(domain.__dict__)
# {
#         'expiration_date': datetime.datetime(2020, 9, 14, 0, 0),
#         'last_updated': datetime.datetime(2011, 7, 20, 0, 0),
#         'registrar': 'MARKMONITOR INC.',
#         'name': 'google.com',
#         'creation_date': datetime.datetime(1997, 9, 15, 0, 0)
# }
# >>> print(domain.name)
# google.com
# >>> print(domain.expiration_date)
# 2020-09-14 00:00:00
