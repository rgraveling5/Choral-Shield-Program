# Rachael
import datetime

#create class 
class Tickets():
  def __init__(self, ticket_id, customer_id, no_tickets, method):
    self.ticket_id = ticket_id
    self.customer_id = customer_id
    self.no_tickets = no_tickets
    self.method = method

def main():
  print ("Essell Academy Choral Shield Competition Sales")
  print(datetime.datetime.now().year)
  print()
  tickets = get_data()
  calc_total(tickets)
  get_method(tickets)
  display_friday(tickets)


def get_data():
  records = []
  file = open('Test 1.csv')
  for line in file:
    data = []
    data = line.replace('"','').strip().split(",")
    ticket_id = data[0]
    customer_id = data[1]
    no_tickets = int(data[2])
    method = data[3]

    records.append(Tickets(ticket_id, customer_id, no_tickets,method))

  return records

  file.close()

def calc_total(records):
  total = 0

  for x in range(len(records)):
    cost = 0
    if records[x].customer_id[0] == "F":
      cost = cost + 10
    else:
      cost = cost + 5

    cost = cost * records[x].no_tickets
    total = total + cost
  print ("The total amount of money raised for charity is £" + str(total))



def get_method (records):
  #count occurances of website
  website_o = 0
  school_o = 0
  search_w = "W"
  search_s = "S"
  for x in range(len(records)):
    if search_w == records[x].method:
      website_o = website_o + 1
    if search_s == records[x].method:
      school_o = school_o + 1

  if school_o > website_o:
    print("The most popular method of sales is from the school.")
    print()
  else: 
    print("The most popular method of sales is via the website.")
    print()
    

def display_friday(records):
  file = open('output.csv','w')
  
  for x in range(len(records)):
    if records[x].customer_id[0] == "F":
      file.write(f'"{records[x].ticket_id}",{records[x].customer_id},{records[x].no_tickets},"{records[x].method}"\n')

  file.close()

main()