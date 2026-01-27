# Source - https://stackoverflow.com/a/51379007
# Posted by Bostjan, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-22, License - CC BY-SA 4.0

data={
  "company": "TechNova Inc",
  "location": "Bangalore",
  "departments": {
    "Engineering": {
      "manager": "Alice",
      "employees": {
        "E101": {
          "name": "Rahul Sharma",
          "role": "Backend Developer",
          "skills": ["Python", "Django", "PostgreSQL"],
          "projects": [
            {
              "name": "Inventory System",
              "status": "Completed"
            },
            {
              "name": "Order API",
              "status": "Ongoing"
            }
          ]
        },
        "E102": {
          "name": "Priya Raj",
          "role": "Frontend Developer",
          "skills": ["React", "CSS", "Figma"],
          "projects": [
            {
              "name": "Customer Portal",
              "status": "Completed"
            }
          ]
        }
      }
    },
    "Marketing": {
      "manager": "David",
      "employees": {
        "M201": {
          "name": "Kiran Desai",
          "role": "SEO Analyst",
          "skills": ["Google Analytics", "Content Strategy"],
          "campaigns": {
            "Q1": "Lead Gen Campaign",
            "Q2": "Brand Awareness"
          }
        }
      }
    }
  }
}

def flatten_data(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

print(flatten_data(data))