
class CuboSpecial:

    def __init__(self, bot):
        self.bot = bot

    def what_problem(self, list_elements):
        try:
            for i in list_elements:
                if i.get_attribute("class") == "content ng-star-inserted":
                    inside_text = i.find_elements_by_xpath(".//*")
                    for j in inside_text:
                        if j.get_attribute("class") == "text":
                            return j.text
        except Exception as e:
            print(e)
            return None


    def pitch(self, list_elements):
        try:
            link = None
            pitch = None
            for i in list_elements:
                if i.get_attribute("class") == "content ng-star-inserted":
                    inside = i.find_elements_by_xpath(".//*")
                    for j in inside:
                        if j.get_attribute("title") == "Video do Pitch":
                            link = j.get_attribute("src")
                        elif j.get_attribute("class") == "text":
                            pitch = str(j.text)

                        if link != None and pitch != None:
                            break

            return link, pitch
        except Exception as e:
            print(e)
            return None, None

    def diff(self, list_elements):
        try:
            for i in list_elements:
                if i.get_attribute("class") == "content ng-star-inserted":
                    inside_text = i.find_elements_by_xpath(".//*")
                    for j in inside_text:
                        if j.get_attribute("class") == "text":
                            return j.text
                            
        except Exception as e:
            print(e)
            return None

    def business(self, list_elements):
        try:
            business = None
            for i in list_elements:
                if i.get_attribute("class") == "list--h":
                    business_list = i.find_elements_by_xpath(".//*")
                    for j in business_list:
                        if business == None:
                            business = j.text
                        else:
                            business = business + " - " + j.text
            return business

        except Exception as e:
            print(e)
            return None
        
    def founders(self, list_elements):
        try:
            founders = None
            for i in list_elements:
                inside = i.find_elements_by_xpath(".//*")
                for j in inside:
                    if j.get_attribute("class") == "ng-star-inserted":
                        if founders == None:
                            founders = str(j.get_attribute("href"))
                        else:
                            founders = founders + " - " + str(j.get_attribute("href"))
            return founders

        except Exception as e:
            print(e)
            return None

    def clients(self, list_elements):
        try:
            clients = None
            for i in list_elements:
                if i.text != "Clients":
                    if clients == None:
                        clients = i.text
                    else:
                        clients = clients + " - " + str(i.text)
            
            return clients

        except Exception as e:
            print(e)
            return None

    def socials(self, list_elements):
        try:
            linkedin = None
            facebook = None
            instagram = None
            twitter = None

            for i in list_elements:
                inside = i.find_elements_by_xpath(".//*")
                for j in inside:
                    if j.get_attribute("title") == "Ver linkedin":
                        linkedin = j.get_attribute("href")
                    elif j.get_attribute("title") == "Ver facebook":
                        facebook = j.get_attribute("href")
                    elif j.get_attribute("title") == "Ver instagram":
                        instagram = j.get_attribute("href")
                    elif j.get_attribute("title") == "Ver twitter":
                        twitter = j.get_attribute("href")

            return linkedin, facebook, instagram, twitter
            
        except Exception as e:
            print(e)
            return None, None, None

    def area(self, list_elements):
        try:
            area = None
            for i in list_elements:
                if i.get_attribute("class") == "content":
                    if area == None:
                        area =  i.text
                    else:
                        area = area + " - " +  i.text
            return area

        except Exception as e:
            print(e)
            return None

    def core(self, list_elements):
        try:
            core = None
            for i in list_elements:
                if i.get_attribute("class") == "content":
                    if core == None:
                        core =  i.text
                    else:
                        core = core + " - " +  i.text
            return core
        except Exception as e:
            print(e)
            return None

    def vertical(self, list_elements):
        try:
            vertical = None
            for i in list_elements:
                if i.get_attribute("class") == "content":
                    if vertical == None:
                        vertical =  i.text
                    else:
                        vertical = vertical + " - " +  i.text

            return vertical
        except Exception as e:
            print(e)
            return None

    def website(self, list_elements):
        try:
            for i in list_elements:
                if i.get_attribute("class") == "title ng-star-inserted":
                    inside = i.find_elements_by_xpath(".//*")
                    for j in inside:
                        if j.get_attribute("rel") == "noopener noreferrer":
                            return j.get_attribute("href")
        except Exception as e:
            print(e)
            return None