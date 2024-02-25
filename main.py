# from flask import Flask, render_template, redirect, url_for, request, jsonify
# import wikipediaapi
# from GPT import GPT_response
# import re
# import gunicorn
#
# app = Flask(__name__)
#
#
# class WikipediaAPI:
#     def __init__(self, topic):
#         self.topic = topic
#         self.wiki_wiki = wikipediaapi.Wikipedia('wikipedia (sample@example.com)', 'en')
#
#     def get_page(self):
#         return self.wiki_wiki.page(self.topic)
#
#
# class WikiSection:
#     @staticmethod
#     def format_section_text(text):
#         paragraphs = text.split('\n')
#         formatted_text = ''.join(f'<p>{paragraph}</p>' for paragraph in paragraphs if paragraph.strip())
#         return formatted_text
#
#     @staticmethod
#     def print_section_contents(section, depth=2):
#         has_content = False
#         has_text = section.text or any(sub_section.text for sub_section in section.sections)
#         html = ""
#         if has_text:
#             html += f"<h{depth}>{section.title}</h{depth}>"
#             has_content = True
#             if section.text:
#                 html += WikiSection.format_section_text(section.text)
#
#         for sub_section in section.sections:
#             if sub_section.text:
#                 has_content = True
#                 sub_section_html = WikiSection.print_section_contents(sub_section, depth=depth + 1)
#                 html += sub_section_html
#
#         if not has_content:
#             html = f"<h1>{section.title}</h1>"
#             html += "<p>There is no text in this section</p>"
#         return html
#
#
# @app.route('/')
# def index():
#     page = wiki_topic.get_page()
#     # Check if the page exists
#     if page.exists():
#         # Retrieve the sections of the page
#         sections = page.sections
#
#         sections_html = ""
#         for i, section in enumerate(sections):
#             # if section.text or section.sections:
#             sections_html += f"<h3>{i + 1}. {section.title}</h3>"
#
#         return render_template('index.html', sections_html=sections_html, topic=topic_name)
#     else:
#         return "Page does not exist"
#
#
# @app.route('/redirect', methods=['GET'])
# def redirect_to_section():
#     section_index = request.args.get('section_index')
#
#     return redirect(url_for('section', section_index=section_index))
#
#
# @app.route('/section/<section_index>')
# def section(section_index):
#     page = wiki_topic.get_page()
#     sections = page.sections
#
#     # Check if section index is valid
#     if 1 <= int(section_index) <= len(sections):
#         selected_section = sections[int(section_index) - 1]
#         section_html = ""
#         section_html += WikiSection.print_section_contents(selected_section)
#
#         return render_template('section.html', section_html=section_html)
#     else:
#         return "Invalid section number. Please try again."
#
#
# @app.route('/summarize_section/<section_index>')
# def summarize_section(section_index):
#     prompt = "Please summarize the given text. Also, ensure that the paraphrased text does not contain any HTML tags."
#     # Retrieve the sections of the page
#     page = wiki_topic.get_page()
#     sections = page.sections
#
#     # Check if section index is valid
#     if 1 <= int(section_index) <= len(sections):
#         selected_section = sections[int(section_index) - 1]
#         section_text = WikiSection.print_section_contents(selected_section)
#
#         # Use GPT to summarize the section text
#         gpt = GPT_response(section_text, prompt)
#         summarized_text = gpt.prompt_response()
#         # Remove HTML tags using regular expressions
#         summarized_text = re.sub(r'<[^>]*>', '', summarized_text)
#
#         # Replace \n with ', ' to ensure they are interpreted as new lines in JSON
#         summarized_text = summarized_text.replace('\n', ', ')
#
#         # Get the topic name and section name
#         section_name = selected_section.title
#
#         # Create a dictionary containing the paraphrased text, topic name, and section name
#         response_data = {
#             "given_topic": topic_name,
#             "section": section_name,
#             "summarized_text": summarized_text
#         }
#
#         # Return the response as JSON
#         return jsonify(response_data)
#     else:
#         return jsonify({"ERROR": "Invalid section number. Please try again."})
#
#
# @app.route('/paraphrase_section/<section_index>')
# def paraphrase_section(section_index):
#     prompt = "Please paraphrase the given text in one paragraph."
#
#     # Retrieve the sections of the page
#     page = wiki_topic.get_page()
#     sections = page.sections
#
#     # Check if section index is valid
#     if 1 <= int(section_index) <= len(sections):
#         selected_section = sections[int(section_index) - 1]
#         section_text = WikiSection.print_section_contents(selected_section)
#
#         # Use GPT to paraphrase the section text
#         gpt = GPT_response(section_text, prompt)
#         paraphrased_text = gpt.prompt_response()
#
#         # Remove HTML tags using regular expressions
#         paraphrased_text = re.sub(r'<[^>]*>', '', paraphrased_text)
#
#         paraphrased_text = paraphrased_text.replace('\n', ', ')
#
#         # Get the topic name and section name
#         section_name = selected_section.title
#
#         # Create a dictionary containing the paraphrased text, topic name, and section name
#         response_data = {
#             "given_topic": topic_name,
#             "section": section_name,
#             "paraphrased_text": paraphrased_text
#         }
#
#         # Return the response as JSON
#         return jsonify(response_data)
#     else:
#         return jsonify({"ERROR": "Invalid section number. Please try again."})
#
#
# if __name__ == '__main__':
#     topic = "https://en.wikipedia.org/wiki/Shivaji"
#     topic_name = topic.split('/')[-1]
#     wiki_topic = WikipediaAPI(topic_name)
#     app.run(debug=True)


from flask import Flask, render_template, redirect, url_for, request, jsonify
import wikipediaapi
from GPT import GPT_response
import re

app = Flask(__name__)
# Instantiate WikipediaAPI object outside of the route
wiki_topic = None


class WikipediaAPI:
    def __init__(self, topic):
        self.topic = topic
        self.wiki_wiki = wikipediaapi.Wikipedia('wikipedia (sample@example.com)', 'en')

    def get_page(self):
        return self.wiki_wiki.page(self.topic)


class WikiSection:
    @staticmethod
    def format_section_text(text):
        paragraphs = text.split('\n')
        formatted_text = ''.join(f'<p>{paragraph}</p>' for paragraph in paragraphs if paragraph.strip())
        return formatted_text

    @staticmethod
    def print_section_contents(section, depth=2):
        has_content = False
        has_text = section.text or any(sub_section.text for sub_section in section.sections)
        html = ""
        if has_text:
            html += f"<h{depth}>{section.title}</h{depth}>"
            has_content = True
            if section.text:
                html += WikiSection.format_section_text(section.text)

        for sub_section in section.sections:
            if sub_section.text:
                has_content = True
                sub_section_html = WikiSection.print_section_contents(sub_section, depth=depth + 1)
                html += sub_section_html

        if not has_content:
            html = f"<h1>{section.title}</h1>"
            html += "<p>There is no text in this section</p>"
        return html


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<topic_name>', methods=['POST'])
def process_topic(topic_name):
    global wiki_topic  # Declare wiki_topic as global
    topic = request.form['topic']
    topic_name = topic.split('/')[-1]
    wiki_topic = WikipediaAPI(topic_name)
    page = wiki_topic.get_page()

    if page.exists():
        sections = page.sections
        sections_html = ""
        for i, section in enumerate(sections):
            sections_html += f"<h3>{i + 1}. {section.title}</h3>"
        return render_template('topics.html', sections_html=sections_html, topic=topic_name)
    else:
        return jsonify({"ERROR": "The entered page does not exist. Please try again."})


@app.route('/redirect', methods=['GET'])
def redirect_to_section():
    section_index = request.args.get('section_index')
    return redirect(url_for('section', section_index=section_index))


@app.route('/section/<section_index>')
def section(section_index):
    global wiki_topic
    page = wiki_topic.get_page()
    sections = page.sections

    if 1 <= int(section_index) <= len(sections):
        selected_section = sections[int(section_index) - 1]
        section_html = ""
        section_html += WikiSection.print_section_contents(selected_section)
        return render_template('section.html', section_html=section_html, section_index=section_index)
    else:
        return jsonify({"ERROR": "Invalid section number. Please try again."})


@app.route('/summarize_section/<section_index>')
def summarize_section(section_index):
    global wiki_topic
    # Retrieve the page and sections
    page = wiki_topic.get_page()
    sections = page.sections

    # Convert section_index to an integer
    section_index = int(section_index)

    # Check if the section_index is within bounds
    if 1 <= section_index <= len(sections):
        selected_section = sections[section_index - 1]
        section_text = WikiSection.print_section_contents(selected_section)

        # Prepare the prompt for GPT
        prompt = "Please summarize the given text in one paragraph."

        # Generate the summary using GPT
        gpt = GPT_response(section_text, prompt)
        summarized_text = gpt.prompt_response()
        summarized_text = re.sub(r'<[^>]*>', '', summarized_text)
        summarized_text = summarized_text.replace('\n', ', ')

        section_name = selected_section.title

        response_data = {
            "section": section_name,
            "summarized_text": summarized_text
        }

        return jsonify(response_data)
    else:
        return jsonify({"ERROR": "Invalid section number. Please try again."})


@app.route('/paraphrase_section/<section_index>')
def paraphrase_section(section_index):
    global wiki_topic
    prompt = "Please paraphrase the given text in one paragraph."
    page = wiki_topic.get_page()
    sections = page.sections

    if 1 <= int(section_index) <= len(sections):
        selected_section = sections[int(section_index) - 1]
        section_text = WikiSection.print_section_contents(selected_section)

        gpt = GPT_response(section_text, prompt)
        paraphrased_text = gpt.prompt_response()
        paraphrased_text = re.sub(r'<[^>]*>', '', paraphrased_text)
        paraphrased_text = paraphrased_text.replace('\n', ', ')

        section_name = selected_section.title

        response_data = {
            "section": section_name,
            "paraphrased_text": paraphrased_text
        }

        return jsonify(response_data)
    else:
        return jsonify({"ERROR": "Invalid section number. Please try again."})


if __name__ == '__main__':
    app.run(debug=True)
