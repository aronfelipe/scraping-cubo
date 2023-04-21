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
        print(startups)
        print(len(startups))
        for startup in startups:
            self.report.insert_startup(link_cubo=startup.get_attribute('href'))

        print(self.report.df_startup)

        for index, row in self.report.df_startup.iterrows():
            self.bot.get(row['Link cubo'])

            time.sleep(10)

            core = None
            area = None
            vertical = None
            name = None
            link = None
            pitch = None
            problem = None
            diff = None
            business = None
            founders = None
            clients = None
            linkedin = None
            facebook = None
            instagram = None
            twitter = None

            list_name_xpath = ["/html/body/app-cubo/main/page-startups-detail/section/div/app-header-company/p",
                        "/html/body/app-cubo/main/page-startups-detail/section/div/app-header-company/p[1]"]

            for i in list_name_xpath:
                try:
                    name = self.bot.find_xpath(i, "text")
                    row["Nome"] = str(name)
                    break
                except:
                    name = None

            list_xpath = [
                "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[1]/article/*",
                "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[2]/article/cb-accordion/*",
                "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[3]/article/cb-accordion/*",
                "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[4]/article/cb-accordion/*",
                "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[5]/article/*",
                "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[6]/article/*",
                "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[7]/article/*",
                "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[8]/article/*",
                "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[9]/article/*",
                "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[10]/article/*"
            ]

            for i in list_xpath:
                xpath = self.bot.find_all_xpath(i, "find")
                for j in xpath:

                    if j.get_attribute("class") == "subsection ng-star-inserted":
                        inside = j.find_elements_by_xpath(".//*")
                        for k in inside:
                            if k.get_attribute("class") == "title":
                                if str(k.text) == "Area":
                                    area = self.special.area(inside)
                                elif str(k.text) == "Core Business":
                                    core = self.special.core(inside)
                                elif str(k.text) == "Vertical":
                                    vertical = self.special.vertical(inside)

                    elif j.get_attribute("class") == "header":

                        if str(j.text) == "What problem do we solve?":
                            problem = self.special.what_problem(xpath)
                            row["What problem do we solve"] = str(problem)
                            break

                        elif str(j.text) == "Pitch":
                            link, pitch = self.special.pitch(xpath)
                            row["Pitch"] = str(pitch)
                            row["Link"] = str(link)
                            break

                        elif str(j.text) == "Market Differentials":
                            diff = self.special.diff(xpath)
                            row["Market Differentials"] = str(diff)
                            break
                
                    elif j.get_attribute("class") == "title ng-star-inserted":

                        if str(j.text) == "Business Model":
                            business = self.special.business(xpath)
                            row["Bussiness Model"] = str(business)
                            break

                        elif str(j.text) == "Founders":
                            founders = self.special.founders(xpath)
                            row["Founders"] = str(founders)
                            break

                        elif str(j.text) == "Clients":
                            clients = self.special.clients(xpath)
                            row["Clients"] = str(clients)
                            break   
                            
                        elif str(j.text) == "Socials Network":
                            linkedin, facebook, instagram, twitter = self.special.socials(xpath)
                            row["Instagram"] = str(instagram)
                            row["Facebook"] = str(facebook)
                            row["Twitter"] = str(twitter)
                            row["Linkedin"] = str(linkedin)
                            break
            
            print("_________________")
            print(area)
            print(core)
            print(vertical)
            print("_________________")

            print("_________________")
            print(linkedin)
            print(facebook)
            print(instagram)
            print(twitter)

            print("_________________")

                    
            # row["Nome"] = str(name)
            # row["Core business"] = str(core)
            # row["Vertical"] = str(vertical)
            # row["Area"] = str(area)
            # row["What problem do we solve"] = str(problem)
            # row["Pitch"] = str(pitch)
            # row["Link"] = str(link)
            # row["Market Differentials"] = str(diff)
            # row["Bussiness Model"] = str(business)
            # row["Founders"] = str(founders)
            # row["Clients"] = str(clients)
            # row["Instagram"] = str(instagram)
            # row["Facebook"] = str(facebook)
            # row["Twitter"] = str(twitter)
            # row["Linkedin"] = str(linkedin)




            # try:
            #     first = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[1]/article/*", "find")

            #     for i in first:

            #         # if i.get_attribute("title") == "Area":

            #         if i.find_element_by_xpath(".//h1[@class='title']").text == "Area":
            #             _area = i.find_elements_by_xpath(".//cb-chip-list/*")
            #             for j in _area:
            #                 if core == "":
            #                     area =  j.find_element_by_xpath(".//div").text
            #                 else:
            #                     area = area + " - " +  j.find_element_by_xpath(".//div").text

            #         elif i.find_element_by_xpath(".//h1[@class='title']").text == "Core Business":
            #             _core = i.find_elements_by_xpath(".//cb-chip-list/*")
            #             for j in _core:
            #                 if core == "":
            #                     core =  j.find_element_by_xpath(".//div").text
            #                 else:
            #                     core = core + " - " +  j.find_element_by_xpath(".//div").text

            #         elif i.find_element_by_xpath(".//h1[@class='title']").text == "Vertical":
            #             _vertical = i.find_elements_by_xpath(".//cb-chip-list/*")
            #             for j in _vertical:
            #                 if vertical == "":
            #                     vertical =  j.find_element_by_xpath(".//div").text
            #                 else:
            #                     vertical = vertical + " - " +  j.find_element_by_xpath(".//div").text

 

            # except Exception as e:
            #     print(e)
            #     pass

            # try:
            #     second = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[2]/article/cb-accordion/*", "find")
            #     # print(second)
            #     problem = None
            #     pitch = None
            #     link = None
            #     for i in second:
            #         print(i.get_attribute("class"))
            #         # if i.find_element_by_xpath(".//*[contains(text(), 'What problem do we solve?')]"):
            #         #     print("AQUI")
            #         if i.get_attribute("class") == "header":
            #             # print(i.text)
            #             if str(i.text) == "What problem do we solve?":

            #                 problem = self.special.what_problem(second)
            #                 break
            #             elif str(i.text) == "Pitch":
            #                 link, pitch = self.special.pitch(third)
            #                 break
            #             elif str(i.text) == "Market Differentials":
            #                 diff = self.special.diff(third)
            #                 break

            #             # else if str(i.text) == ""
            #         # if i.get_attribute("class") == "content ng-star-inserted":
            #         #     inside_text = i.find_elements_by_xpath(".//*")
            #         #     for j in inside_text:
            #         #         print(j.get_attribute("class"))
            #         #         if j.get_attribute("class") == "text":
            #         #             problem = j.text

            #     # print(problem)

            #         # if i.find_element_by_xpath(".//*[contains(text(), 'What problem do we solve?')]"):
            #         #     text = i.find_element_by_class_name("text").text
            #         #     print(text)
            #         #     inside = i.find_elements_by_xpath(".//section/*")
            #         #     for j in inside:
            #         #         print(j.find_element_by_xpath(".//app-translator/div").text)
            #         #         problem = j.find_element_by_xpath(".//app-translator/div").text


            #     # print(problem)

            # except Exception as e:
            #     print(e)
            #     problem = None


            # try:
            #     third = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[3]/article/cb-accordion/*", "find")
                
            #     for i in third:

            #         if i.get_attribute("class") == "header":

            #             if str(i.text) == "What problem do we solve?":
            #                 problem = self.special.what_problem(third)
            #                 break
            #             elif str(i.text) == "Pitch":
            #                 link, pitch = self.special.pitch(third)
            #                 break
            #             elif str(i.text) == "Market Differentials":
            #                 diff = self.special.diff(third)
            #                 break

            # except Exception as e:
            #     print(e)

            # try:
            #     fourth = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[4]/article/cb-accordion/*", "find")
                
            #     for i in fourth:

            #         if i.get_attribute("class") == "header":

            #             if str(i.text) == "What problem do we solve?":
            #                 problem = self.special.what_problem(fourth)
            #                 break
            #             elif str(i.text) == "Pitch":
            #                 link, pitch = self.special.pitch(fourth)
            #                 break
            #             elif str(i.text) == "Market Differentials":
            #                 diff = self.special.diff(fourth)
            #                 break

            # except Exception as e:
            #     print(e)


            # try:
            #     fifth = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[5]/article/*", "find")
                
            #     for i in fifth:

            #         if i.get_attribute("class") == "header":

            #             if str(i.text) == "What problem do we solve?":
            #                 problem = self.special.what_problem(fifth)
            #                 break
            #             elif str(i.text) == "Pitch":
            #                 link, pitch = self.special.pitch(fifth)
            #                 break
            #             elif str(i.text) == "Market Differentials":
            #                 diff = self.special.diff(fifth)
            #                 break
                
            #         elif i.get_attribute("class") == "title ng-star-inserted":
            #             if str(i.text) == "Business Model":
            #                 business = self.special.business(fifth)
            #                 break

            # except Exception as e:
            #     print(e)

            # try:
            #     sixth = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[6]/article/*", "find")
                
            #     for i in sixth:

            #         if i.get_attribute("class") == "header":

            #             if str(i.text) == "What problem do we solve?":
            #                 problem = self.special.what_problem(sixth)
            #                 break
            #             elif str(i.text) == "Pitch":
            #                 link, pitch = self.special.pitch(sixth)
            #                 break
            #             elif str(i.text) == "Market Differentials":
            #                 diff = self.special.diff(sixth)
            #                 break
                
            #         elif i.get_attribute("class") == "title ng-star-inserted":
            #             if str(i.text) == "Business Model":
            #                 business = self.special.business(sixth)
            #                 break

            #             elif str(i.text) == "Founders":
            #                 founders = self.special.founders(sixth)
            #                 print(founders)
            #                 break

            # except Exception as e:
            #     print(e)

            # try:
            #     list_xpath = ["/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[8]/article/*",
            #                   "/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[7]/article/*"]

            #     for xpath in list_xpath:
            #         seventh = self.bot.find_all_xpath(xpath, "find")
            #         for i in seventh:

            #             if i.get_attribute("class") == "header":

            #                 if str(i.text) == "What problem do we solve?":
            #                     problem = self.special.what_problem(seventh)
            #                     break
            #                 elif str(i.text) == "Pitch":
            #                     link, pitch = self.special.pitch(seventh)
            #                     break
            #                 elif str(i.text) == "Market Differentials":
            #                     diff = self.special.diff(seventh)
            #                     break
                    
            #             elif i.get_attribute("class") == "title ng-star-inserted":
            #                 if str(i.text) == "Business Model":
            #                     business = self.special.business(seventh)
            #                     break

            #                 elif str(i.text) == "Founders":
            #                     founders = self.special.founders(seventh)
            #                     break

            #                 elif str(i.text) == "Clients":
            #                     clients = self.special.clients(seventh)
            #                     break   

            # except Exception as e:
            #     print(e)

            # try:
            #     eighth = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[10]/article/*", "find")

            #     for i in eighth:

            #         if i.get_attribute("class") == "header":

            #             if str(i.text) == "What problem do we solve?":
            #                 problem = self.special.what_problem(eighth)
            #                 break
            #             elif str(i.text) == "Pitch":
            #                 link, pitch = self.special.pitch(eighth)
            #                 break
            #             elif str(i.text) == "Market Differentials":
            #                 diff = self.special.diff(eighth)
            #                 break
                
            #         elif i.get_attribute("class") == "title ng-star-inserted":
            #             if str(i.text) == "Business Model":
            #                 business = self.special.business(eighth)
            #                 break

            #             elif str(i.text) == "Founders":
            #                 founders = self.special.founders(eighth)
            #                 break

            #             elif str(i.text) == "Clients":
            #                 clients = self.special.clients(eighth)
            #                 break   
                            
            #             elif str(i.text) == "Socials Network":
            #                 linkedin, facebook, instagram, twitter = self.special.socials(eighth)
            #                 break

            # except Exception as e:
            #     print(e)

            # try:
            #     website = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[9]/article/a", "text")
            # except:
            #     website = None

            # try:
            #     address = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[10]/article/address/span", "text")
            # except:
            #     try:
            #         address = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[11]/article/address/span", "text")
            #     except:
            #         address = None


            # row["Website"] = str(website)
            # row["Address"] = str(address)
            # print(self.report.df_startup)

            if index > 3:
                break

        self.report.df_startup.to_csv("startup.csv", index = False)

chrome_path = r"/home/felipe/Documents/chromedriver"
url = "https://cubo.network/startups"
element = "/html/body/app-cubo/app-header/header/a/img"

cubo = CuboSearch(chrome_path=chrome_path, url=url, element=element)
cubo.loop()