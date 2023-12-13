# Script can be used for filtering the appl repos from product scrop2 and scrop2plus
# Pass the "scrop2" or "scrop2plus" value in main function

# Importing modules
import yaml
import subprocess

# Function to get the product file in scrop2 or scrop2plus
def get_group_vars_file(product_name: str):
    #Creating temp directory
    result = subprocess.run("mktemp -d", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    temp_dir = result.stdout.strip()
    print(temp_dir)
    #Clone the repo in temp directory
    command = f"git clone https://gitlab.collaborationlayer-traton.com/ats-project/ats-project-group/scania-ats/ats-product-{product_name}.git"
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", cwd=temp_dir)
    group_vars_file = f"{temp_dir}/ats-product-{product_name}/group_vars/{product_name}.yml"
    return group_vars_file

# Function to save the application repos
def save_applications(product_name):
    group_vars_file = get_group_vars_file(product_name)
    with open(group_vars_file, "r") as f:
        file_content = yaml.safe_load(f)
    
    appl_scope = file_content["artifacts"]
    unique_appls = list()
    appl_file = open(f"{product_name}_appl_repos.txt", "w")
    for appl, appl_dict in appl_scope.items():
        # Application which has a verion is an APPL repo
        if appl_dict["version"] is not None:
            appl_repo = appl_dict['application']
            # To get unique applications (avoid duplicates)
            if appl_repo not in unique_appls:
                unique_appls.append(appl_repo)
                # Write appl_repo to the file {product_name}_appl_repos.txt
                appl_file.write(f"{appl_repo}\n")
    appl_file.close()
    # Open and read the file after writing:
    appl_file = open(f"{product_name}_appl_repos.txt", "r")
    print(appl_file.read())

# Main function to pass values, scrop2 or scrop2plus
if __name__ == "__main__":
    save_applications("scrop2")
