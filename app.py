from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Admission Inquiry Chatbot API!'})

@app.route('/api/generate-response', methods=['POST'])
def generate_response():
    try:
        data = request.json
        user_message = data.get('message', '').lower().strip()
        user_id = data.get('user_id')
        response = {}

        # Expanded small talk responses
        if any(greeting in user_message for greeting in ['hello', 'hi', 'hey','namaste']):
            response = {'reply': 'Hello ! How can I assist you with your admission inquiries today ?', 'buttons': []}
        elif 'how are you' in user_message:
            response = {'reply': "I'm just a bot, but I'm here to help! How can I assist you?", 'buttons': []}
        elif 'thank you' in user_message or 'thanks' in user_message:
            response = {'reply': "You're welcome! If you have more questions, feel free to ask.", 'buttons': []}
        elif 'what is your name' in user_message:
            response = {'reply': "I'm the Admission Inquiry Bot for Graphic Era Hill University, Bhimtal Campus!", 'buttons': []}
        elif 'bye' in user_message or 'goodbye' in user_message:
            response = {'reply': "Goodbye! Feel free to reach out anytime you have questions about admissions!", 'buttons': []}
        elif 'what can you do' in user_message:
            response = {'reply': "I can assist you with information about our courses, admission process, campus facilities, and more!",
                        'buttons': []}

        # College-specific responses
        elif 'graphic era' in user_message or 'gehu' in user_message:
            response = {
                'reply': 'Graphic Era Hill University, Bhimtal Campus, is a premier institution offering world-class education in the foothills of the Himalayas. '
                         'Would you like to know more about our 30 years of academic excellence, courses, admission process, or campus facilities?',
                'buttons': [
                    {'text': '30 Years of Excellence', 'action': '30-years-excellence'},
                    {'text': 'Courses Offered', 'action': 'courses'},
                    {'text': 'Admission Process', 'action': 'admission-process'},
                    {'text': 'Campus Facilities', 'action': 'campus-facilities'}
                ]
            }
        elif 'admission process' in user_message:
            response = {
                'reply': 'Our admission process is straightforward. You can apply online, and we also conduct counseling sessions for interested candidates. '
                         'Would you like more details on how to apply?',
                'buttons': [
                    {'text': 'Yes', 'action': 'apply-now'},
                    {'text': 'No', 'action': 'no-thanks'}
                ]
            }
        elif 'apply-now' in user_message or 'yes' in user_message:
            response = {
                'reply': 'You can find more details about the admission process and apply online on our [enquiry page](https://www.gehu.ac.in). If you have any more questions, feel free to ask!',
                'buttons': []
            }
        elif 'no-thanks' in user_message or 'no' in user_message:
            response = {
                'reply': 'Thank you for reaching out! If you have any more questions in the future, don’t hesitate to ask. Have a great day!',
                'buttons': []
            }

        elif 'top placements' in user_message:
            response = {
                'reply': 'Our students enjoy consistently high placements at top MNCs like Amazon, Uber, TCS, American Express and more. '
                         'We strive to provide our students with the best career opportunities, and our exceptional placements serve as a testament to our efforts.',
                'buttons': []
            }
        elif 'merit based scholarships' in user_message:
            response = {
                'reply': 'We offer merit-based scholarships in all courses for the entire duration of the program. '
                         'We believe in recognizing and supporting the academic achievements of our students and helping them achieve their full potential.',
                'buttons': []
            }
        elif 'additional scholarships' in user_message:
            response = {
                'reply': 'We strive to ensure that deserving children are not deprived of the opportunity and tools to flourish in the world. '
                         'Therefore, we offer a 25% concession for domiciles of hill states, a 10% additional scholarship for female candidates, '
                         'and a 5% fee concession for wards of defense personnel.',
                'buttons': []
            }
        elif 'accreditations and rankings' in user_message:
            response = {
                'reply': 'Our university holds top-tier rankings and accreditations, some of which are exclusive to the region. '
                         'We have earned these recognitions through our unwavering commitment to providing the highest quality education and experiences to our students.',
                'buttons': []
            }
        elif 'courses offered' in user_message or 'what courses do you offer' in user_message:
            response = {
                'reply': "We offer a variety of undergraduate and postgraduate programs. Please select a course to learn more:",
                'buttons': [
                    {'text': 'BCA', 'action': 'bca'},
                    {'text': 'BTech', 'action': 'btech'},
                    {'text': 'Mechanical', 'action': 'mechanical'},
                    {'text': 'Civil', 'action': 'civil'},
                    {'text': 'Management', 'action': 'management'},
                    {'text': 'Commerce', 'action': 'commerce'},
                    {'text': 'Pharmacy', 'action': 'pharmacy'},
                    {'text': 'Nursing', 'action': 'nursing'},
                    {'text': 'Polytechnic', 'action': 'polytechnic'},
                    {'text': 'Allied Science', 'action': 'allied-science'}
                ]
            }
        elif 'bca' in user_message:
            response = {
                'reply': 'The BCA program at Graphic Era Hill University is designed to provide students with a strong foundation in computer applications and software development. The curriculum includes programming languages, web development, and database management.',
                'buttons': []
            }
        elif 'btech' in user_message:
            response = {
                'reply': 'Our BTech program offers specializations in various branches such as Computer Science, Mechanical, Civil, Electrical, and Electronics Engineering. It aims to equip students with the technical skills required to excel in their respective fields.',
                'buttons': []
            }
        elif 'mechanical' in user_message:
            response = {
                'reply': 'The Mechanical Engineering program focuses on the design, analysis, and manufacturing of mechanical systems. Students learn about thermodynamics, fluid mechanics, and materials science.',
                'buttons': []
            }
        elif 'civil' in user_message:
            response = {
                'reply': 'The Civil Engineering program covers the planning, design, and construction of infrastructure projects such as buildings, roads, and bridges. It emphasizes structural engineering, environmental engineering, and construction management.',
                'buttons': []
            }
        elif 'management' in user_message:
            response = {
                'reply': 'Our Management program prepares students for leadership roles in business and industry. It covers areas such as finance, marketing, human resources, and operations management.',
                'buttons': []
            }
        elif 'commerce' in user_message:
            response = {
                'reply': 'The Commerce program provides a comprehensive understanding of business principles, accounting, finance, and economics. It prepares students for careers in business, banking, and finance.',
                'buttons': []
            }
        elif 'pharmacy' in user_message:
            response = {
                'reply': 'The Pharmacy program offers in-depth knowledge of pharmaceutical sciences, including drug development, pharmacology, and clinical practice. It prepares students for careers in healthcare and the pharmaceutical industry.',
                'buttons': []
            }
        elif 'nursing' in user_message:
            response = {
                'reply': 'The Nursing program is designed to prepare students for a rewarding career in healthcare. It covers patient care, medical procedures, and health education, ensuring that graduates are ready to work in hospitals and clinics.',
                'buttons': []
            }
        elif 'polytechnic' in user_message:
            response = {
                'reply': 'Our Polytechnic program offers diploma courses in various engineering disciplines, providing hands-on technical education and practical skills for students looking to enter the workforce quickly.',
                'buttons': []
            }
        elif 'allied science' in user_message:
            response = {
                'reply': 'The Allied Science program includes courses in biotechnology, microbiology, and environmental science. It prepares students for careers in research, healthcare, and environmental management.',
                'buttons': []
            }
        elif '30 years' in user_message or 'excellence' in user_message:
            response = {
                'reply': 'Graphic Era Educational Society (GEES) was established in 1993 with the mission to provide world-class education. Over 30 years, '
                         'GEES has achieved numerous milestones, starting as the first self-financed institute in North India offering engineering courses. '
                         'Our founder, Prof. Kamal Ghanshala, envisioned providing holistic professional education, which became a reality with the Graphic Era Group Of Institutions.',
                 'buttons': [
                    {'text': 'Locations', 'action': 'locations'},
                    {'text': 'Other Campuses', 'action': 'other-campuses'}
                ]
            }
        elif 'locations' in user_message:
            response = {
                'reply': 'Graphic Era Hill University, Bhimtal Campus is located in the scenic foothills of the Himalayas. For detailed location information, please visit our website.',
                'buttons': []
            }
        elif 'other-campuses' in user_message or 'Other Campuses' in user_message:
            response = {
                'reply': 'In addition to the Bhimtal campus, Graphic Era Hill University has two more campuses: the Halwani Campus and the Dehradun Campus. Each campus offers a unique set of programs and facilities. Would you like more information about any specific campus?',
                'buttons': [
                    {'text': 'Bhimtal Campus', 'action': 'bhimtal-campus'},
                    {'text': 'Halwani Campus', 'action': 'halwani-campus'},
                    {'text': 'Dehradun Campus', 'action': 'dehradun-campus'}
                ]
            }
        elif 'bhimtal-campus' in user_message or 'bhimtal campus' in user_message:
            response = {
                'reply': 'The Bhimtal Campus is situated in the picturesque Kumaon foothills, offering state-of-the-art facilities and a serene environment for academic pursuits.',
                'buttons': []
            }
        elif 'halwani-campus' in user_message:
            response = {
                'reply': 'The Halwani Campus is located in a strategic area providing various undergraduate and postgraduate programs with a focus on industry integration.',
                'buttons': []
            }
        elif 'dehradun-campus' in user_message:
            response = {
                'reply': 'The Dehradun Campus, situated in the capital city of Uttarakhand, offers a range of programs and benefits from being in a major educational hub.',
                'buttons': []
            }
        elif 'courses' in user_message:
            response = {
                'reply': 'We offer a variety of undergraduate and postgraduate programs in Engineering, Management, Humanities, and Applied Sciences. '
                         'Would you like to know more about a specific course?',
                'buttons': []
            }

        elif 'campus facilities' in user_message:
            response = {
                'reply': 'Our Bhimtal Campus is a self-contained community with state-of-the-art academic and research facilities, modern laboratories, well-stocked libraries, and more.',
                'buttons': [
                    {'text': 'Library', 'action': 'library'},
                    {'text': 'Laboratories', 'action': 'laboratories'},
                    {'text': 'Hostel Facilities', 'action': 'hostel-facilities'}
                ]
            }
        elif 'library' in user_message:
            response = {
                'reply': 'Our campus library is well-equipped with the latest books, journals, and digital resources, providing students with access to world-class knowledge and research.',
                'buttons': []
            }
        elif 'laboratories' in user_message:
            response = {
                'reply': 'Our laboratories are equipped with modern equipment and tools, allowing students to gain hands-on experience in their respective fields of study.',
                'buttons': []
            }
        elif 'hostel facilities' in user_message:
            response = {
                'reply': 'We offer comfortable and safe hostel facilities with all essential amenities, ensuring a conducive environment for students to study and relax.',
                'buttons': []
            }
        else:
            response = {'reply': "Sorry, I didn't understand that. Can you please rephrase or ask about something else?", 'buttons': []}

        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
