# Ask your PDF - Talk to your PDFs with the power of AI

Introducing "Ask your PDF": it's like having a friendly chat right within your Python application, but with a twist – you can now have conversations with multiple PDF documents! Imagine being able to ask questions about these PDFs using natural language, just like you would with a friend, and getting back answers that really make sense because they're based on what's in those documents. This awesome app relies on a smart language model to whip up accurate responses to all your queries. But remember, it's worth noting that the app's chit-chat skills are solely focused on the uploaded PDFs. With "Ask your PDF" by your side, research tasks become an absolute breeze, making information discovery smoother than ever.

The PDF Query Tool is a powerful Python program that revolutionizes how you interact with PDF documents. By harnessing the capabilities of cutting-edge libraries such as LangChain, PyPDF2, Streamlit, OpenAI, Hugging Face's Hub, and InstructorEmbedding, this tool enables you to ask complex questions about the content of your PDFs and receive insightful answers.

## Key Features

1. **Advanced Language Processing:** The program leverages LangChain to preprocess and understand natural language queries. This allows you to interact with your PDFs in a conversational manner, making your interactions feel more intuitive and natural.

2. **PDF Content Extraction:** PyPDF2 is used to accurately extract text and metadata from your PDF documents. This extracted content forms the basis for answering your queries effectively.

3. **Seamless Interaction:** Thanks to the Streamlit library, the program offers a user-friendly and interactive interface. You can easily upload your PDFs, input questions, and receive detailed responses in a visually appealing manner.

4. **AI-powered Responses:** By integrating OpenAI's powerful language models, the program comprehends your questions and provides detailed, contextually relevant answers. It understands the nuances of your queries and extracts meaningful information from your PDFs to deliver accurate responses.

5. **Efficient Search:** The combination of FAISS-CPU and Altair enables fast and efficient content searching within your PDFs. You can search for keywords, phrases, or concepts across multiple PDFs with remarkable speed.

6. **Tokenization and Embeddings:** The program utilizes tiktoken to tokenize your text data, making it ready for further analysis. InstructorEmbedding and Sentence-Transformers then generate rich embeddings that capture the essence of the text, enhancing the accuracy of question-answering and search processes.

7. **Seamless Integration:** Hugging Face's Hub allows you to seamlessly integrate state-of-the-art NLP models, ensuring that you have access to the latest advancements in the field for optimal performance.

**How It Works:**

1. **Upload PDFs:** Simply upload or select prexisting PDF documents using the user-friendly interface.

2. **Ask Questions:** Input your questions related to the content of the PDFs. The program understands the context and intent of your queries.

3. **Receive Answers:** Receive comprehensive answers that draw from the content of your PDFs. The program extracts relevant information and presents it to you in a clear and concise manner.

4. **Explore and Search:** Utilize the search functionality to quickly locate specific information within your PDFs. The tool's integration of FAISS-CPU ensures that your searches are lightning-fast.

5. **Visualize Insights:** With Altair, the program provides visual representations of key data points and trends found within your PDFs, enhancing your understanding and decision-making.

The program brings together cutting-edge technologies to simplify and enhance your interaction with PDF documents. Whether you're a researcher, student, or professional, this tool empowers you to unlock the wealth of knowledge stored within your PDFs effortlessly. Say goodbye to tedious manual searches and hello to a new era of efficient, AI-driven document exploration.

## Requirements

langchain

PyPDF2

python-dotenv

streamlit

openai

faiss-cpu

altair

tiktoken

For Hugginface install:

huggingface-hub

For Instructor Embedding install:

InstructorEmbedding

sentence-transformers

Copy: pip install langchain PyPDF2 python-dotenv streamlit openai faiss-cpu altair tiktoken huggingface-hub InstructorEmbedding sentence-transformers 
