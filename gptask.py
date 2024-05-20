import openai
import tiktoken
import degreeProgram as dP
api_key = "input-key"
client = openai.OpenAI(api_key=api_key)

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def schedule_student(
    model="gpt-3.5-turbo",
    major= 'Agricultural & Extension Education, B.S',
    concentration = "Agricultural Leadership and Development",
    previous: list = []
):

    degree = dP.read_major(dP.open_major(major), concentration)

    previous_str = "\n".join(previous)

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": """You are a college advisor building a schedule for an incoming student. 
                The courses the student previously took are listed below as well as the requirements for the student's degree. 
                Please build a schedule for only one semester listing the Department (The capital letters at the start of the course name) and ID (The four numbers after the department).
                For all electives (courses with no department name and number) please select a specific course in it's place. All courses should only be taken once. The schedule should be in json format"""
             + "The Requirements for the student's specific degree: " + degree + "\n\n---\n\n Courses taken previously by student: "+ previous_str +"\nAnswer:"},
        ]
    )

    print(completion.choices[0].message.content)

schedule_student(major="Computer Science, B.S.", concentration="Cloud Computing and Networking", previous=['CSC 1350', 'ENGL 1001', 'GEOL 1001'])