import streamlit as st
import joblib

def main():
# to create Fore Header for our Web App, here i have created HTML template
	html_temp = """ <div style="background-color: lightyellow; padding:16px"> <h2 style = "color:green"; text-align:center> Health Insurance Cost Prediction using ML </h2> </div> """

# and to use this HTML template here i have used 'markdown' function of streamlit library
	st.markdown(html_temp, unsafe_allow_html = True)

# now if you want run this code to see how the sample output is, go to command prompt "C:\Users\surendra\Desktop>streamlit run webapp.py" and press Enter

# Now Let me first Load our model
	model = joblib.load('model_joblib_gr')
# Now after loading this model, let me create first Age and it is 'int', so for that i am taking 'slider' from this streamlit
	p1 = st.slider("Enter your Age ", 18,100)

# Next is Sex
	s1 = st.selectbox('Sex ', ('Male', 'Female'))
# Please remember this is String, but for the prediction we require Integer value;
# so let me map to 0 and 1
	if s1=='Male':
		p2=1
	else :
		p2=0

# Next is BMI value
	p3 = st.number_input("Enter your BMI value ")

# Next is Number of Children
	p4 = st.slider("Enter Number of Children ", 0,4)

# Next is Smoker or not
	s2 = st.selectbox("Smoker", ("Yes", "No"))
# here again it is String, now map it to 0 and 1
	if s2 == "Yes":
		p5=1
	else:
		p5=0

# Next is Region
	p6 = st.slider("Enter your Region ", 1,4)

# Now lets create 'Predict' Button
	if st.button('Predict') :
		pred=model.predict([[p1,p2,p3,p4,p5,p6]])
	
		st.balloons()	# It gives some fun type balloons animation 
		st.success('Your Insurance cost is {}'.format(round(pred[0],2)))	# 2 means 2 decimal places


if __name__ == '__main__' :
	main()