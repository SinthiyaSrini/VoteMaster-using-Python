nominee1 = input("Enter nominee1 name: ")
nominee2 = input("Enter nominee2 name: ")

nom1_vote = 0
nom2_vote = 0

vote_id = list(range(1, 1000))

num_of_voters = len(vote_id)

while True:
    voter = input("Enter your voter ID number (or type 'exit' to stop): ")

    if voter.lower() == 'exit':  
        print("Voting session is terminated early.")
        if nom1_vote > nom2_vote:
            
            percent = (nom1_vote / num_of_voters) * 100
            print(nominee1, "has won with", percent, "% votes.")
        elif nom2_vote > nom1_vote:
            percent = (nom2_vote / num_of_voters) * 100
            print(nominee2, "has won with", percent, "% votes.")
        else:
            print("It's a tie!")
        break
    
    try:
        voter = int(voter) 
    except ValueError:
        print("Invalid input. Please enter a valid voter ID number or 'exit'.")
        continue

    if voter in vote_id:  
        print("You are a voter.")
        vote_id.remove(voter) 
        vote = int(input("Enter your vote (1 for {} or 2 for {}): ".format(nominee1, nominee2)))
        if vote == 1:
            nom1_vote += 1
            print("Thank you for your vote.")
        elif vote == 2:
            nom2_vote += 1
            print("Thank you for your vote.")
        else:
            print("Invalid vote option. Please vote 1 or 2.")
    else:
        print("You have already voted or you are not eligible.")