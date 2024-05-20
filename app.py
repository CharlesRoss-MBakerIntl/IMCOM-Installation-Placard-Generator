import streamlit as st
import re




style_container = """


<style>
    .image-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .image-link {
        position: relative;
        display: inline-block;
        overflow: hidden; /* Hide overflow if images are larger */
        margin: 15px 0; /* Adjust vertical and horizontal spacing */
    }
    .image-link img {
        display: block;
        width: 350px; /* Set a fixed width */
        height: 300px; /* Set a fixed height */
        object-fit: cover; /* Maintain aspect ratio and fill container */
    }
    .overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(254,195,37,0.5);
            opacity: 0; /* Initially transparent */
            transition: opacity 0.3s; /* Add transition for smooth appearance */
            pointer-events: none; /* Allow clicks to go through the overlay */
        }
    .image-link:hover .overlay {
        opacity: 1; /* Show overlay on hover */
    }
    .text-overlay {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 10px;
        font-size: 25px;
        text-align: center;
        z-index: 1; /* Ensure text is above the image */
    }
</style>
"""






# Define the main function for the Streamlit app
def main():
    
    st.title('IMCOM Installation Placard Generator')

    st.write("#")


    with st.form("placard_form"):
        
        st.write("Enter Title for Placards")
        title = st.text_input(label = "Section Title", value = '', key = 'title')
        
        st.write("#")
        st.write("#")

        st.write("Enter information for Placard 1:")
        name_1 = st.text_input(label="Installation Name", value="", key='name_1')
        image_1 = st.text_input(label="Image Link", value="", key='image_1')
        link_1 = st.text_input(label="Page Link", value="", key='link_1')
        
        st.write('#')

        st.write("Enter information for Placard 2:")
        name_2 = st.text_input(label="Installation Name", value="", key='name_2')
        image_2 = st.text_input(label="Image Link", value="", key='image_2')
        link_2 = st.text_input(label="Page Link", value="", key='link_2')

        st.write('#')

        st.write("Enter information for Placard 3:")
        name_3 = st.text_input(label="Installation Name", value="", key='name_3')
        image_3 = st.text_input(label="Image Link", value="", key='image_3')
        link_3 = st.text_input(label="Page Link", value="", key='link_3')

        st.write("#")

        st.write("Enter information for Placard 4:")
        name_4 = st.text_input(label="Installation Name", value="", key='name_4')
        image_4 = st.text_input(label="Image Link", value="", key='image_4')
        link_4 = st.text_input(label="Page Link", value="", key='link_4')

        st.write("#")

        st.write("Enter information for Placard 5:")
        name_5 = st.text_input(label="Installation Name", value="", key='name_5')
        image_5 = st.text_input(label="Image Link", value="", key='image_5')
        link_5 = st.text_input(label="Page Link", value="", key='link_5')

        st.write("#")

        st.write("Enter information for Placard 6:")
        name_6 = st.text_input(label="Installation Name", value="", key='name_6')
        image_6 = st.text_input(label="Image Link", value="", key='image_6')
        link_6 = st.text_input(label="Page Link", value="", key='link_6')

        st.write("#")


        placard_info = {}

        if name_1.strip() and image_1.strip() and link_1.strip():
            placard_info['placard_1'] = {'name': name_1,
                                         'image': image_1,
                                         'link': link_1}

        if name_2.strip() and image_2.strip() and link_2.strip():
            placard_info['placard_2'] = {'name': name_2,
                                         'image': image_2,
                                         'link': link_2}

        if name_3.strip() and image_3.strip() and link_3.strip():
           placard_info['placard_3'] = {'name': name_3,
                                         'image': image_3,
                                         'link': link_3}

        if name_4.strip() and image_4.strip() and link_4.strip():
            placard_info['placard_4'] = {'name': name_4,
                                         'image': image_4,
                                         'link': link_4}

        if name_5.strip() and image_5.strip() and link_5.strip():
            placard_info['placard_5'] = {'name': name_5,
                                         'image': image_5,
                                         'link': link_5}

        if name_6.strip() and image_6.strip() and link_6.strip():
            placard_info['placard_6'] = {'name': name_6,
                                         'image': image_6,
                                         'link': link_6}


        #Create DIV Container
        div_container = """
        <div class="image-container">

        """

        #Add Code to DIV Container
        for key, value in placard_info.items():

            placard = placard_info[key]

            placard_container = f"""

            <a href={placard['link']} class="image-link">
                    <img src={placard['image']} alt="Image">
                    <div class="text-overlay">{placard['name']}</div>
            </a>

            """

            div_container += placard_container + "\n"


        #Close the DIV Container
        div_container += "</div>"



        #Create Title Contaienr
        title_container = f"""
        <h4>{title}</h4>
        """


           
        # Create Final Container

        final_container = f"""
        
        {title_container}
        {style_container}
        {div_container}

        """
            
        
    

    
        
        submit = st.form_submit_button(label="Generate HTML Code")

        

    if submit:
        st.code(final_container)








# Run the Streamlit app
if __name__ == "__main__":
    main()