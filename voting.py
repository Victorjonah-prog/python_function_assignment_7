"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""



candidates = {}
voters = set()

def register_candidates(*args, **kwargs):
    """Register candidates with optional metadata.
    """
    for candidate in args:
        candidates[candidate] = 0
    print(candidates)
register_candidates("Jon", "Mayor", "Trump", party = "PPP")

def cast_vote(voter_id, candidate):
    """Cast vote if voter has not voted before.
        after all the vote logic is completeted sucessfully,
        return: Vote casted for {candidate}.
    """
    if voter_id in voters:
        print(f"Voter with ID{voter_id} has already voted")
        return
    else:
        for candids in candidates:
            if candids == candidate:
                candidates[candidate] += 1
                print(candidates)
        else:
            return"Candidate does not exist!"
    print(voters)
    print(candidates)
cast_vote(1, "mp")
cast_vote(2, "k9ine")
cast_vote(3, "tosin")
cast_vote(1, "mark")
def election_result():
    """Return the winner(s)."""
    # max_votes = #add logic
    max_votes = 0
    for candidate in candidates:
        if candidates[candidate] > max_votes:
            max_votes = candidates[candidate]
    # winners = #add logic
    for candidate in candidates:
        if candidates[candidate] == max_votes:
            winner = candidate
    return {"winners": winner, "candidates": candidates}
print(election_result())
