from covid import Covid

covid = Covid()

cname = input("Country name  ")
cname = covid.get_status_by_country_name(cname)
# print(covid.list_countries())
data = {
    key: cname[key]
    for key in cname.keys() and{
        'confirmed',
        'active',
        'deaths',
        'recovered'
    }
}
print(data)
