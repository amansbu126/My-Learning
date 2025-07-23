from loguru import logger
import pandas as pd

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

rows=[]

# Log company and location info first
logger.info(f"Company: {data['company']}")
logger.info(f"Location: {data['location']}")

# Now loop through departments and employees
import pandas as pd

rows = []

for dept_name, dept_info in data["departments"].items():
    for emp_id, emp_info in dept_info["employees"].items():
        row = {
            "Company": data["company"],
            "Location": data["location"],
            "Department": dept_name,
            "Employee ID": emp_id,
            "Name": emp_info.get("name"),
            "Role": emp_info.get("role"),
            "Skills": ", ".join(emp_info.get("skills", [])),
            "Campaigns": ", ".join(emp_info.get("campaigns", {}).values()) if "campaigns" in emp_info else None
        }
        rows.append(row)

# Convert to DataFrame
df = pd.DataFrame(rows)

# Print
print(df)
