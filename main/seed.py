from main.models import Project


projects = [

     # EmpowerAbility
    {
        "title": "EmpowerAbility",

        "description":
        "An assistive technology platform combining computer vision and IoT to detect mobility impairments and automatically adjust environments.",

        "technologies":
        "Python ML ComputerVision Mediapipe YOLO Torch Streamlit",

        "source_code":
        "https://github.com/connectspawan/EmpowerAbility",

        "live_demo":
        "https://drive.google.com/file/d/1u5Gn2UtXT-O85qaScmxrrBcZw_0SHTFm/view"
    },

]


for item in projects:

    Project.objects.create(
        title=item["title"],
        description=item["description"],
        technologies=item["technologies"],
        source_code=item["source_code"],
        live_demo=item["live_demo"],
        image="projects/default.png"
    )


print("All Projects Added Successfully")