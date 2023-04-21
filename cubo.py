import time
from report import CuboReport
from scraping import ScrapScrap
from special import CuboSpecial

class CuboSearch:

    def __init__(self, chrome_path, url, element):
        self.bot = ScrapScrap(chrome_path=chrome_path)
        self.bot.get(url)
        time.sleep(5)
        self.bot.get(url)
        self.bot.wait(element)

        self.special = CuboSpecial(self.bot)
        self.report = CuboReport()
        self.report.create_df_startup()

        # for i in range(0, 50):
        #     self.bot.scroll_down()
        #     time.sleep(1)

        # self.bot.maximize()
        
    def loop(self):

        startups = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-list/section/div[4]/div/*[@class='startups__item ng-star-inserted']", "find")

        startups_link_list = []

        for startup in startups:
            startups_link_list.append(startup.get_attribute('href'))


        counter = 0

        for link_cubo in startups_link_list:

            if counter == 3:
                break
            
            counter += 1



            name = None
            core = None
            area = None
            vertical = None
            problem = None
            link = None
            pitch = None
            diff = None
            business = None
            founders = None
            clients = None
            instagram = None
            facebook = None
            twitter = None
            linkedin = None
            website = None
            address = None

            self.bot.get(link_cubo)

            time.sleep(10)

            list_name = ["/html/body/app-cubo/main/page-startups-detail/section/div/app-header-company/p",
                        "/html/body/app-cubo/main/page-startups-detail/section/div/app-header-company/p[1]"]

            for i in list_name:
                try:
                    name = self.bot.find_xpath(i, "text")
                    break
                except:
                    name = None


            try:
                first = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[1]/article/*", "find")
                core = ""
                area = ""
                vertical = ""
                for i in first:

                    if i.find_element_by_xpath(".//h1[@class='title']").text == "Area":
                        _area = i.find_elements_by_xpath(".//cb-chip-list/*")
                        for j in _area:
                            if core == "":
                                area =  j.find_element_by_xpath(".//div").text
                            else:
                                area = area + " - " +  j.find_element_by_xpath(".//div").text

                    elif i.find_element_by_xpath(".//h1[@class='title']").text == "Core Business":
                        _core = i.find_elements_by_xpath(".//cb-chip-list/*")
                        for j in _core:
                            if core == "":
                                core =  j.find_element_by_xpath(".//div").text
                            else:
                                core = core + " - " +  j.find_element_by_xpath(".//div").text

                    elif i.find_element_by_xpath(".//h1[@class='title']").text == "Vertical":
                        _vertical = i.find_elements_by_xpath(".//cb-chip-list/*")
                        for j in _vertical:
                            if vertical == "":
                                vertical =  j.find_element_by_xpath(".//div").text
                            else:
                                vertical = vertical + " - " +  j.find_element_by_xpath(".//div").text

            except Exception as e:
                print(e)
                pass

            try:
                second = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[2]/article/cb-accordion/*", "find")
                # print(second)
                problem = None
                pitch = None
                link = None
                for i in second:
                    # print(i.get_attribute("class"))
                    # if i.find_element_by_xpath(".//*[contains(text(), 'What problem do we solve?')]"):
                    #     print("AQUI")
                    if i.get_attribute("class") == "header":
                        # print(i.text)
                        if str(i.text) == "What problem do we solve?":

                            problem = self.special.what_problem(second)
                            break
                        elif str(i.text) == "Pitch":
                            link, pitch = self.special.pitch(third)
                            break
                        elif str(i.text) == "Market Differentials":
                            diff = self.special.diff(third)
                            break

                        # else if str(i.text) == ""
                    # if i.get_attribute("class") == "content ng-star-inserted":
                    #     inside_text = i.find_elements_by_xpath(".//*")
                    #     for j in inside_text:
                    #         print(j.get_attribute("class"))
                    #         if j.get_attribute("class") == "text":
                    #             problem = j.text

                # print(problem)

                    # if i.find_element_by_xpath(".//*[contains(text(), 'What problem do we solve?')]"):
                    #     text = i.find_element_by_class_name("text").text
                    #     print(text)
                    #     inside = i.find_elements_by_xpath(".//section/*")
                    #     for j in inside:
                    #         print(j.find_element_by_xpath(".//app-translator/div").text)
                    #         problem = j.find_element_by_xpath(".//app-translator/div").text


                # print(problem)

            except Exception as e:
                print(e)
                problem = None


            try:
                third = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[3]/article/cb-accordion/*", "find")
                
                for i in third:

                    if i.get_attribute("class") == "header":

                        if str(i.text) == "What problem do we solve?":
                            problem = self.special.what_problem(third)
                            break
                        elif str(i.text) == "Pitch":
                            link, pitch = self.special.pitch(third)
                            break
                        elif str(i.text) == "Market Differentials":
                            diff = self.special.diff(third)
                            break

            except Exception as e:
                print(e)

            try:
                fourth = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[4]/article/cb-accordion/*", "find")
                
                for i in fourth:

                    if i.get_attribute("class") == "header":

                        if str(i.text) == "What problem do we solve?":
                            problem = self.special.what_problem(fourth)
                            break
                        elif str(i.text) == "Pitch":
                            link, pitch = self.special.pitch(fourth)
                            break
                        elif str(i.text) == "Market Differentials":
                            diff = self.special.diff(fourth)
                            break

            except Exception as e:
                print(e)


            try:
                fifth = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[5]/article/*", "find")
                
                for i in fifth:

                    if i.get_attribute("class") == "header":

                        if str(i.text) == "What problem do we solve?":
                            problem = self.special.what_problem(fifth)
                            break
                        elif str(i.text) == "Pitch":
                            link, pitch = self.special.pitch(fifth)
                            break
                        elif str(i.text) == "Market Differentials":
                            diff = self.special.diff(fifth)
                            break
                
                    elif i.get_attribute("class") == "title ng-star-inserted":
                        if str(i.text) == "Business Model":
                            business = self.special.business(fifth)
                            break

            except Exception as e:
                print(e)

            try:
                sixth = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[6]/article/*", "find")
                
                for i in sixth:

                    if i.get_attribute("class") == "header":

                        if str(i.text) == "What problem do we solve?":
                            problem = self.special.what_problem(sixth)
                            break
                        elif str(i.text) == "Pitch":
                            link, pitch = self.special.pitch(sixth)
                            break
                        elif str(i.text) == "Market Differentials":
                            diff = self.special.diff(sixth)
                            break
                
                    elif i.get_attribute("class") == "title ng-star-inserted":
                        if str(i.text) == "Business Model":
                            business = self.special.business(sixth)
                            break

                        elif str(i.text) == "Founders":
                            founders = self.special.founders(sixth)
                            break

            except Exception as e:
                print(e)

            try:
                list_xpath = ["/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[8]/article/*",
                              "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[7]/article/*"]

                for xpath in list_xpath:
                    seventh = self.bot.find_all_xpath(xpath, "find")
                    for i in seventh:

                        if i.get_attribute("class") == "header":

                            if str(i.text) == "What problem do we solve?":
                                problem = self.special.what_problem(seventh)
                                break
                            elif str(i.text) == "Pitch":
                                link, pitch = self.special.pitch(seventh)
                                break
                            elif str(i.text) == "Market Differentials":
                                diff = self.special.diff(seventh)
                                break
                    
                        elif i.get_attribute("class") == "title ng-star-inserted":
                            if str(i.text) == "Business Model":
                                business = self.special.business(seventh)
                                break

                            elif str(i.text) == "Founders":
                                founders = self.special.founders(seventh)
                                break

                            elif str(i.text) == "Clients":
                                clients = self.special.clients(seventh)
                                break   

            except Exception as e:
                print(e)

            try:
                eighth = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[10]/article/*", "find")

                for i in eighth:

                    if i.get_attribute("class") == "header":

                        if str(i.text) == "What problem do we solve?":
                            problem = self.special.what_problem(eighth)
                            break
                        elif str(i.text) == "Pitch":
                            link, pitch = self.special.pitch(eighth)
                            break
                        elif str(i.text) == "Market Differentials":
                            diff = self.special.diff(eighth)
                            break
                
                    elif i.get_attribute("class") == "title ng-star-inserted":
                        if str(i.text) == "Business Model":
                            business = self.special.business(eighth)
                            break

                        elif str(i.text) == "Founders":
                            founders = self.special.founders(eighth)
                            break

                        elif str(i.text) == "Clients":
                            clients = self.special.clients(eighth)
                            break   
                            
                        elif str(i.text) == "Socials Network":
                            linkedin, facebook, instagram, twitter = self.special.socials(eighth)
                            break

                        elif str(i.text) == "Website":
                            website = self.special.website(eighth)
                            break

            except Exception as e:
                print(e)

            try:
                ninth = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[11]/article/*", "find")
                

                for i in ninth:

                    if i.get_attribute("class") == "header":

                        if str(i.text) == "What problem do we solve?":
                            problem = self.special.what_problem(ninth)
                            break
                        elif str(i.text) == "Pitch":
                            link, pitch = self.special.pitch(ninth)
                            break
                        elif str(i.text) == "Market Differentials":
                            diff = self.special.diff(ninth)
                            break
                
                    elif i.get_attribute("class") == "title ng-star-inserted":
                        if str(i.text) == "Business Model":
                            business = self.special.business(ninth)
                            break

                        elif str(i.text) == "Founders":
                            founders = self.special.founders(ninth)
                            break

                        elif str(i.text) == "Clients":
                            clients = self.special.clients(ninth)
                            break   
                            
                        elif str(i.text) == "Socials Network":
                            linkedin, facebook, instagram, twitter = self.special.socials(ninth)
                            break

                        elif str(i.text) == "Website":
                            website = self.special.website(ninth)
                            break

            except Exception as e:
                print(e)
            # try:
            #     address = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[10]/article/address/span", "text")
            # except:
            #     try:
            #         address = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[11]/article/address/span", "text")
            #     except:
            #         address = None

            self.report.insert_startup(link_cubo=link_cubo, name=name,
            core=core, area=area, vertical=vertical, problem=problem,link_pitch=link,
            pitch=pitch, diff=diff, business=business, founders=founders,
            clients=clients, instagram=instagram, facebook=facebook,
            twitter=twitter, linkedin=linkedin, website=website, address=address)

        self.report.df_startup.to_csv("startup.csv", index = False)

chrome_path = r"/home/felipe/Documents/chromedriver"
url = "https://cubo.network/startups"
element = "/html/body/app-cubo/app-header/header/a/img"

cubo = CuboSearch(chrome_path=chrome_path, url=url, element=element)
cubo.loop()