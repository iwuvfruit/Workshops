#get the top stared repos in github using github api 
import requests

#I want a specific language
def create_query(languages, min_stars=50000):
	query = f"stars:>{min_stars} " #query github expects
	for language in languages:
		query += f"language:{language} "
	return query 



def repos_with_most_stars():
	gh_api_repo_search_url = "https://api.github.com/search/repositories"
	parameters = {"q":"stars:50000"} #specific parameter to github api
	response = requests.get(gh_api_repo_search_url, params=parameters) #we put an argument called params
	#print(response.text)
	#response_json = response.json()
	#print(response_json.keys()) 
	# we see the key items is the one we are interested in 
	response_json = response.json()["items"] #we get the values using items key
	return response_json #will return list of items


if __name__ == "__main__": #dunder main
	#have a main method here
	#pass
	results = repos_with_most_stars()
	languages = ["Python", "Javascript"]

	#print(len(results))
	#first_result = results[0]
	#print(first_result)
	for result in results: #another dictionary
		langauge = result["language"]
		stars = result["stargazers_count"]
		name = result["name"]

		print(f"->{name} is a {language} with{stars}")


#type comes back with api it'll be converted that matches python
#if return with a list of objects ->list of dictionaries 
#search api needs a query, it says code:mssing 
