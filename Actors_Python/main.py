
def read_in_actor_Info():
    actor_names = []
    actor_ages = []
    top_films = []
    film_earnings_mills = []

    num_actors = 0

    actor_info = open("Actors.txt","r")

    for line in actor_info:
    
        temporary_list_row_data = line.split(',')
    
        actor_names.append(temporary_list_row_data[0])
        actor_ages.append(int(temporary_list_row_data[1]))
        top_films.append(temporary_list_row_data[2])
        film_earnings_mills.append(float(temporary_list_row_data[3]))
    
        num_actors = num_actors + 1

    actor_info.close()

    return actor_names, actor_ages, top_films, film_earnings_mills, num_actors

def counting_occurance(num_actors, film_earnings_mills):

 target = 0

 print("Enter a Value in millions to search for: £ " ,end=" ")
 target = float(input())
 
 count = 0
 for x in range(num_actors):
   if film_earnings_mills[x] > target:
     count = count+1

 print(count, "Actors earn over £",target, "Million")
 print("-----------")


 return num_actors, film_earnings_mills

def output_info_screen(actor_names, actor_ages, top_films, film_earnings_mills, num_actors):
   
    print ("Actors info ")
    print("-----------")
    print ()
    for x in range (num_actors):
        print ("Actor", actor_names[x],"is", actor_ages[x],"making currently around",film_earnings_mills[x],"million per film with top rated film currently as",top_films[x],".")
        print("")
    return


def output_info_file(actor_names, actor_ages, top_films, film_earnings_mills, num_actors):    

    output_file = open("ActorInfoSentences.txt","w")                           

    for x in range(num_actors):

        output_file.write("Actor " + actor_names[x] + " is " + str(actor_ages[x]) + " making currently around " + str(film_earnings_mills[x]) + "million per film with top rated film currently as " + top_films[x] + ".\n\n")

    output_file.close()

    return


actor_names, actor_ages, top_films, film_earnings_mills, num_actors = read_in_actor_Info()

numberofactors, filmearnings = counting_occurance(num_actors, film_earnings_mills)

output_info_screen(actor_names, actor_ages, top_films, film_earnings_mills, num_actors)


output_info_file(actor_names, actor_ages, top_films, film_earnings_mills, num_actors)