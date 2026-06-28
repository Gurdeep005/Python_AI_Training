# AI ENGINEER--  An AI Engineer is a software developer who builds practical, production-ready AI applications.
#                Instead of building complex AI models from scratch, they focus on integrating existing pre-trained 
#                models(like LLMs) and AI APIs into real world systems, optimizing user experience and ensuring 
#                scalability and safety.
#                AI > ML > DL > LLM

#-------------------------------------------------------------------------------------------------------------------------

# AI--  Artificial Intelligence is the ability of a machine or computer to perform tasks that normally require human
#       intelligence.
#  eg. ->
#     * ChatGPT
#     * Siri & Google Assistant
#     * self-driving cars
#     * Face recognisation in smartphones
#     * Recommendation systems on Youtube & Netflix

#  Goal of AI ->  To make machines:-
#     * Learn                     * Reason
#     * Understand language       * Solve problems
#     * Make Decisions

#--------------------------------------------------------------------------------------------------------------------------

# ML--  Machine learning is a subset of AI. Instead of directly programming every rule, we just provide data and the
#       machine learns patterns from that data.

#  Eg:- Suppose you want to identify whether an e-mail is spam.
#      * Traditional Programming ->   Rules + Data  ->  Output
#      * Machine Learning ->    Data + Output  ->  Model
# The model learns the rules automatically.

# Applications ->
#      * Spam detection
#      * Stock prediction
#      * Product recommendations

# Types of ML:-
#   1) Supervised Learning:-  In this, the model learns from labelled data.
#                             Labelled data means the correct answer is already provided.

# Eg:-
  
#   Input          Output
#   Spam Email     Spam
#   Email          Not Spam

# The model learns from these examples & predicts      for new emails.

#  Applications ->
#      * Spam detection
#      * House Price Prediction
#      * Student result prediction

#   2) Unsupervised Learning:-  In this, the data has no labels.  
#                               The model tries to find patterns or groups on its own.
# Eg:-
#      Suppose a shopping website has customer data but doesn't have customer categories.

#  The model may create groups like ->
#      * High spenders
#      * Medium spenders
#      * New shoppers

# Applications ->
#      * Customer segmentation
#      * Market analysis
#      * Recommendation systems
#      * Pattern detection

#  3) Reinforcement Learning:-       In this, an agent learns by interacting with an environment.

# It receives ->
#      * Reward for correct actions
#      * Penalty for wrong actions
# The goal is to maximize rewards.

#  Eg:- Teaching a dog:-
#      * Correct tricks -> Reward
#      * Wrong trick -> No reward
# Similarly, the AI learns through trial & error.

#  Applications ->
#      * Self-driving cars
#      * Robotics
#      * Game playing

#  4) Semi-supervised Learning:-  This combines supervised and unsupervised learning.
#                                 The dataset contains ->
#                                                        * A small amount of labelled data.
#                                                        * A large amount of unlabelled data.     
#  Eg:- Out of 10,000 images:-
#      * 1,000 are labelled
#      * 9,000 are unlabelled
# The model uses both to improve learning.

#  Applications ->
#      * Image recognition
#      * Speech recognition
#      * Medical diagnosis

# NOTE:- Which type of ML is used by ChatGPT?
#     -> ChatGPT is based on Deep Learning (a subset of ML), and is trained using a combination of:-
#                         * Supervised Learning
#                         * Reinforcement Learning from Human Feedback (RLHF)

#----------------------------------------------------------------------------------------------------------------------------

# DL--  Deep Learning is a subset of ML.
#       It uses Artificial Neural Networks inspired by the human brain.

# Why DL?
#   It handles ->
#         * Images
#         * Voice
#         * Video
#         * Natural Language

#  Eg:-
#       * Face recognition
#       * Self-driving cars
#       * Medical image analysis

#-----------------------------------------------------------------------------------------------------------------------------

# LLM--  Large Language Model
#        It is a DL model trained on huge amounts of text data.

#  Eg:-
#      * OpenAI ChatGPT
#      * Google Gemini
#      * Meta Llama
#      * Claude

# What can LLMs do?
#      * Answer questions
#      * Generate code
#      * Write emails
#      * Translate languages
#      * Summarize text
#      * Create content

# How LLMs work?
#      * Train on massive data
#      * Learn language patterns
#      * Predict the next word