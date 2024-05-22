import streamlit as st
import re




style_container = """


<style>
    .page_title {
        font-weight: 300;
        line-height: 120%;
        margin: 20px 0;
        text-shadow: 0 1px 5px rgba(0,0,0,.8);
        text-transform: uppercase;
    }
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

    placard_info = {}
    


    st.title('IMCOM Installation Placard Generator')

    st.write("#")

        
    st.markdown("##### Select Placard Container Information")
    st.write('######')
    
    
    #FIRST PANEL?
    first_panel = st.radio('Is this the first panel for the IMCOM Page:', ['Yes', 'No'])
    
    if first_panel == 'Yes':
        
        # IMCOM TITLE
        imcom_title = st.text_input(label = "IMCOM Title", value = '', key = 'imcom_title', placeholder="Eg: Training, Sustainment, Readiness, Pacific, Europe")

        st.write("#")

    if first_panel == 'No':
        imcom_title = ''


    if first_panel:
        
        # IS this the first section of panels for the group
        first_section = st.radio('Is this the first section of 6 installations for the group:', ['Yes', 'No'])

        if first_section == "Yes":
                
                title = st.text_input(label = "Group Title", value = '', key = 'title', placeholder="Eg: AIGP Tier - Foundation Pathway, AIGP Tier - Gold, Local Portal")

        if first_section == "No":
            title = ''
                
                
    if first_panel and first_section:   
                
        st.write("#")
        st.write("#")

        st.markdown("##### Enter information for Installation 1:")
        name_1 = st.text_input(label="Installation Name", value="", key='name_1')
        image_1 = st.text_input(label="Image Link", value="", key='image_1')
        link_1 = st.text_input(label="Page Link", value="", key='link_1')
        
        st.write('#')
        st.write('#')

        placard_info['placard_1'] = {'name': name_1,
                                            'image': image_1,
                                            'link': link_1}
            
        if image_1 == '':
            placard_info['placard_1']['image'] = 'https://aigp-iigg.obs.army.mil/portal/sharing/rest/content/items/e8aec440a8a747cebb25c4572c2d1ab2/data'



        if name_1 and image_1 and link_1:
            st.markdown("##### Enter information for Installation 2:")
            name_2 = st.text_input(label="Installation Name", value="", key='name_2')
            image_2 = st.text_input(label="Image Link", value="", key='image_2')
            link_2 = st.text_input(label="Page Link", value="", key='link_2')
            
            st.write('#')
            st.write('#')

            placard_info['placard_2'] = {'name': name_2,
                                            'image': image_2,
                                            'link': link_2}
            
            if image_2 == '':
                placard_info['placard_2']['image'] = 'https://aigp-iigg.obs.army.mil/portal/sharing/rest/content/items/36536602c0c7482ea8ad5f5e6fbfb897/data'



            if name_2 and image_2 and link_2:
                st.markdown("##### Enter information for Installation 3:")
                name_3 = st.text_input(label="Installation Name", value="", key='name_3')
                image_3 = st.text_input(label="Image Link", value="", key='image_3')
                link_3 = st.text_input(label="Page Link", value="", key='link_3')

                st.write("#")
                st.write("#")

                placard_info['placard_3'] = {'name': name_3,
                                            'image': image_3,
                                            'link': link_3}
            
                if image_3 == '':
                    placard_info['placard_3']['image'] = 'https://aigp-iigg.obs.army.mil/portal/sharing/rest/content/items/8d8a7d38f08b40f09817be43e5acc42f/data'



                if name_3 and image_3 and link_3:
                    st.markdown("##### Enter information for Installation 4:")
                    name_4 = st.text_input(label="Installation Name", value="", key='name_4')
                    image_4 = st.text_input(label="Image Link", value="", key='image_4')
                    link_4 = st.text_input(label="Page Link", value="", key='link_4')

                    st.write("#")
                    st.write("#")

                    placard_info['placard_4'] = {'name': name_4,
                                            'image': image_4,
                                            'link': link_4}
            
                    if image_4 == '':
                        placard_info['placard_4']['image'] = 'https://aigp-iigg.obs.army.mil/portal/sharing/rest/content/items/cb8f7627fb45439f97e73d92690ab023/data'



                    if name_4 and image_4 and link_4:
                        st.markdown("##### Enter information for Installation 5:")
                        name_5 = st.text_input(label="Installation Name", value="", key='name_5')
                        image_5 = st.text_input(label="Image Link", value="", key='image_5')
                        link_5 = st.text_input(label="Page Link", value="", key='link_5')

                        st.write("#")
                        st.write("#")

                        placard_info['placard_5'] = {'name': name_5,
                                            'image': image_5,
                                            'link': link_5}
            
                        if image_5 == '':
                            placard_info['placard_5']['image'] = 'https://aigp-iigg.obs.army.mil/portal/sharing/rest/content/items/02e9aaaa4a5f4c22b7ce14420696cf0d/data'


                        if name_5 and image_5 and link_5:
                            st.markdown("##### Enter information for Installation 6:")
                            name_6 = st.text_input(label="Installation Name", value="", key='name_6')
                            image_6 = st.text_input(label="Image Link", value="", key='image_6')
                            link_6 = st.text_input(label="Page Link", value="", key='link_6')

                            st.write("#")
                            st.write("#")

                            placard_info['placard_6'] = {'name': name_6,
                                            'image': image_6,
                                            'link': link_6}
            
                            if image_6 == '':
                                placard_info['placard_6']['image'] = 'https://aigp-iigg.obs.army.mil/portal/sharing/rest/content/items/ddb6ac04beda46c2b0dfcd8d48b135f6/data'


                            
                            
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

        #Create IMCOM Title Container
        imcom_container = f"""<h1 class="page_title">{imcom_title}</h1>"""

            
        # Create Final Container
        if imcom_title != '' and title != '':

            final_container = f"""
                                {imcom_container}{title_container}
                                {style_container}
                                {div_container}

                                """
            
        elif imcom_title == '' and title != '':
            
            final_container = f"""
                                    {title_container}
                                    {style_container}
                                    {div_container}

                                    """
            
        elif imcom_title == '' and title == '':
            
            final_container = f"""
                                    {style_container}
                                    {div_container}

                                    """

                            

        
        submit = st.button("Generate Code")
            
        if submit:
            st.code(final_container)
    
    
    

        

    








# Run the Streamlit app
if __name__ == "__main__":
    main()