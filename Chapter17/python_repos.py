import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

names, plot_dicts = [], []
'''

# Examine the first repository.
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
'''

#names, stars = [], []
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:

    print("\nName:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Created:", repo_dict['created_at'])
    print("Updated:", repo_dict['updated_at'])
    if repo_dict['description']:
        print("Description:", repo_dict['description'])
    else:
        print("Description: ")

    names.append(repo_dict['name'])
    #stars.append(repo_dict['stargazers_count'])
    star = repo_dict['stargazers_count']
    if repo_dict['description']:
        desc = repo_dict['description']
    else:
        desc = 'None'
    if repo_dict['html_url']:
        url = repo_dict['html_url']
    else:
        url = 'None'
    plot_dict = {
        'value': star,
        'label': desc,
        'xlink': url,
    }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

#chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
chart.render_in_browser()

'''
# Process results.
print(response_dict.keys())
'''

