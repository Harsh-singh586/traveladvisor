
from bs4 import BeautifulSoup
from requests_html import HTMLSession
class New_York:

	def gethotels(self):

		html_list = []

		link_list = []

		session = HTMLSession()

		base_url = 'https://www.tripadvisor.com/Hotels-g60763-oa{a}-New_York_City_New_York-Hotels.html'

		for k in range(60, 910, 30):
			link_list.append(base_url.format(a = k))

		for link in link_list:
			html_list.append(session.get(link))

		details = []

		for r in html_list:

			hotel_init = BeautifulSoup(r.content, 'html.parser')

			hotel_list = hotel_init.find_all('div', attrs = {'data-prwidget-name' : 'meta_hsx_responsive_listing'})

			for i in hotel_list:
				try:
					print('a')
					hotel_detail = {}
					details_field = ['name', 'price', 'rating', 'image_link', 'tripadvisor_link']
					unique_key = i.find('div', attrs = {'class' : 'meta_listing'})['data-locationid']
					name = i.find('div', attrs = {'class' : 'listing_title'}).text.split('    ')[1].strip()
					hotel_detail['name'] = name
					price_list_scrap = i.find_all('div', attrs = {'class' : 'text-link'})
					vendors_price = []
					for vendor in price_list_scrap:
						vendor_name = vendor.find('div', attrs = {'class' : 'vendor'}).text.strip()
						price = vendor.find('div', attrs = {'class' : 'price'}).text.strip()
						vendor_detail = {'vendor_name' : vendor_name, 'vendor_price' : price}
						vendors_price.append(vendor_detail)
					additionl_vendor = i.find('div', attrs = {'class' : 'provider'}).text.strip()
					additionl_vendor_price = i.find('div', attrs = {'class' : 'price-wrap'}).text.strip()
					vendors_price.append({'vendor_name' : additionl_vendor, 'vendor_price' : additionl_vendor_price})
					hotel_detail['prices'] = vendors_price
					hotel_rating = i.find('a', attrs = {'class' : 'ui_bubble_rating'})['alt'].split('of')[0].strip()
					hotel_detail['rating'] = float(hotel_rating)
					image_link = i.find('img')['src']
					hotel_detail['image_link'] = image_link
					tripadvisor_link = i.find('a', attrs = {'class' : 'respListingPhoto'})['href']
					add_head_tripadvisor_link = 'https://tripadvisor.in' + tripadvisor_link
					hotel_detail['tripadvisor_link'] = add_head_tripadvisor_link
					details.append(hotel_detail)
				except Exception as e:
					pass
		return(details)

	def getrestaurants(self):
		session = HTMLSession()
		r = session.get('https://www.google.com/search?rlz=1C1GGRV_enIN964IN964&tbs=lf:1,lf_ui:9&tbm=lcl&sxsrf=AOaemvLJykkvdr1qA10SRm_1DN6P154LpQ:1638681028514&q=restaurants+in+new+york&rflfq=1&num=10&sa=X&ved=2ahUKEwi55OrE8sv0AhU1muYKHeA9C1QQjGp6BAgLEHo&biw=1366&bih=695#rlfi=hd:;si:;mv:[[40.771831,-73.9693392],[40.7043842,-74.01654549999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u5!2m2!5m1!1sgcid_3american_1restaurant!1m4!1u5!2m2!5m1!1sgcid_3french_1restaurant!1m4!1u2!2m2!2m1!1e1!1m4!1u1!2m2!1m1!1e1!1m4!1u1!2m2!1m1!1e2!1m4!1u22!2m2!21m1!1e1!2m1!1e2!2m1!1e5!2m1!1e1!2m1!1e3!3sIAEqAlVT,lf:1,lf_ui:9')
		soup = BeautifulSoup(r.content, 'html.parser')
		next_page_table = soup.find('table', attrs = {'class' : 'AaVjTc'})
		next_page_element = next_page_table.find_all('a', attrs = {'class' : 'fl'})
		next_page_links = []
		for element in next_page_element:
			next_page_links.append('https://www.google.com' + element['href'])
		all_detail_list = []
		for links in next_page_links:
			session = HTMLSession()
			r = session.get(links)
			soup = BeautifulSoup(r.content, 'html.parser')
			restaurants = soup.find_all('div', attrs = {'jsname' : 'GZq3Ke'})
			for i in restaurants:
				try:
					details_field = ['name', 'review', 'avg_cost', 'cuisine', 'description', 'address', 'services']
					ids = i['jsdata'] 
					main_container = i.find('div', attrs = {'class' : 'cXedhc uQ4NLd'})
					if main_container:
						name_container = main_container.find('div', attrs = {'class' : 'dbg0pd'})
						if name_container:
							name = name_container.find('span').text.strip()
						detail_container = main_container.find('div', attrs = {'class' : 'rllt__details'})
						if detail_container:
							detail_divs = detail_container.find_all('div')
							detail_level_one = detail_divs[0]
							review_span_container = detail_level_one.find('span', attrs = {'aria-hidden' : 'true'})
							if review_span_container:
								review = review_span_container.text.strip()
							else:
								review = 'Not Avilable'
							avgcost_span_container = detail_level_one.find_all('span', attrs = {'role' : 'img'})[1]
							if avgcost_span_container:
								avg_cost = avgcost_span_container.text
							else:
								avg_cost = 'Not Avilable'
							predict_cuisine = detail_level_one.text.strip().split('·')[-1]
							if len(predict_cuisine) > 3 and '₹' not in predict_cuisine:
								cuisine = predict_cuisine
							else:
								cuisine = 'Not Avilable'
							address = detail_divs[1].text.strip()
							des_container = detail_container.find('div', attrs = {'class' : 'rllt__wrapped'})
							if des_container:
								des = des_container.text.strip()
							else:
								des = 'Not Available'
							service_container = detail_container.find('div', attrs = {'class' : 'dXnVAb'})
							if service_container:
								services = service_container.text.strip().split('·')
							else:
								services = 'Not Avilable'
							detail_dict = {'ids' : ids, 'name' : name, 'review' : review, 'avg_cost' : avg_cost, 'cuisine' : cuisine, 'description' : des, 'address' : address, 'services' : services} 				
							all_detail_list.append(detail_dict)
				except Exception as e:
					print(e)
		return(all_detail_list)

	def getthingstodo(self):
		session = HTMLSession()
		r = session.get('https://www.google.com/travel/things-to-do/experiences?g2lb=4644488%2C4401769%2C4317915%2C4640247%2C4270442%2C4605861%2C4675050%2C4371335%2C4306835%2C4624411%2C2503771%2C4649664%2C4597339%2C4419364%2C2502548%2C4641139%2C2503781%2C4258168%2C4596364%2C4270859%2C4291517%2C4284970&hl=en-IN&gl=in&cs=1&ssta=1&dest_mid=%2Fm%2F02_286&dest_state_type=sae&dest_src=ts&q=things%20to%20do%20in%20new%20york&sa=X&ved=2ahUKEwiH7J_j88z0AhXmFLcAHeKoBVQQuL0BegQIFBA4#ttdm=40.723123_-74.001735_12&ttdmf=%252Fm%252F02nd_')
		soup = BeautifulSoup(r.content, 'html.parser')
		elements = soup.find_all('div', attrs = {'class' : 'Ld2paf'})
		all_detail = []
		for element in elements:
			details_field = ['name', 'rating', 'description', 'image_link']
			name = element.find('div', attrs = {'class' : 'skFvHc YmWhbc'}).text
			try:
				rating = element.find('div', attrs = {'class' : 'tP34jb'}).text
			except:
				rating = 'Not Available'
			try:
				des = element.find('div', attrs = {'class' : 'nFoFM'}).text
			except:
				des = 'Not Available'
			image_container = element.find('img')
			if image_container:
				image_link =  image_container['data-src']
			else:
				image_link = None
			detail_dic = {'name' : name, 'rating' : rating, 'description' : des, 'image_link' : image_link}
			all_detail.append(detail_dic)
		return(all_detail)

	def getthingstosee(self):
		session = HTMLSession()
		r = session.get('https://www.google.com/travel/things-to-do/places?g2lb=4644488%2C4401769%2C4317915%2C4640247%2C4270442%2C4605861%2C4675050%2C4371335%2C4306835%2C4624411%2C2503771%2C4649664%2C4597339%2C4419364%2C2502548%2C4641139%2C2503781%2C4258168%2C4596364%2C4270859%2C4291517%2C4284970&hl=en-IN&gl=in&cs=1&ssta=1&dest_mid=%2Fm%2F02_286&dest_state_type=sap&dest_src=ts&q=things%20to%20do%20in%20new%20york&sa=X&ved=2ahUKEwiH7J_j88z0AhXmFLcAHeKoBVQQuL0BegQIFBA4#ttdm=40.723123_-74.001735_12&ttdmf=%252Fm%252F02nd_')
		soup = BeautifulSoup(r.content, 'html.parser')
		elements = soup.find_all('div', attrs = {'class' : 'Ld2paf'})
		all_detail = []
		for element in elements:
			details_field = ['name', 'rating', 'description', 'image_link']
			name = element.find('div', attrs = {'class' : 'skFvHc YmWhbc'}).text
			try:
				rating = element.find('div', attrs = {'class' : 'tP34jb'}).text
			except:
				rating = 'Not Available'
			try:
				des = element.find('div', attrs = {'class' : 'nFoFM'}).text
			except:
				des = 'Not Available'
			image_container = element.find('img')
			if image_container:
				image_link =  image_container['data-src']
			else:
				image_link = None
			detail_dic = {'name' : name, 'rating' : rating, 'description' : des, 'image_link' : image_link}
			all_detail.append(detail_dic)
		return(all_detail)


class New_delhi:

	def gethotels(self):

		html_list = []

		link_list = []

		session = HTMLSession()

		base_url = 'https://www.tripadvisor.in/SmartDeals-g304551-New_Delhi_National_Capital_Territory_of_Delhi-Hotel-Deals.html'

		link_list.append(base_url)

		for link in link_list:
			print('a')
			html_list.append(session.get(link))

		print(html_list)

		details = []

		for r in html_list:

			hotel_init = BeautifulSoup(r.content, 'html.parser')

			hotel_list = hotel_init.find_all('div', attrs = {'data-prwidget-name' : 'meta_hsx_responsive_listing'})

			for i in hotel_list:
				try:
					details_field = ['name', 'price', 'rating', 'image_link', 'tripadvisor_link']
					unique_key = i.find('div', attrs = {'class' : 'meta_listing'})['data-locationid']
					name = i.find('div', attrs = {'class' : 'listing_title'}).text.split('    ')[1].strip()
					price_list_scrap = i.find_all('div', attrs = {'class' : 'text-link'})
					vendors_price = []
					for vendor in price_list_scrap:
						vendor_name = vendor.find('div', attrs = {'class' : 'vendor'}).text.strip()
						price = vendor.find('div', attrs = {'class' : 'price'}).text.strip().split('₹\xa0')[1]
						vendor_detail = {'vendor_name' : vendor_name, 'vendor_price' : price}
						vendors_price.append(vendor_detail)
					additionl_vendor = i.find('div', attrs = {'class' : 'provider'}).text.strip()
					additionl_vendor_price = i.find('div', attrs = {'class' : 'price-wrap'}).text.strip().split('₹\xa0')[1]
					vendors_price.append({'vendor_name' : additionl_vendor, 'vendor_price' : additionl_vendor_price})
					hotel_rating = i.find('a', attrs = {'class' : 'ui_bubble_rating'})['alt']
					image_link = i.find('img')['src']
					tripadvisor_link = i.find('a', attrs = {'class' : 'respListingPhoto'})['href']
					add_head_tripadvisor_link = 'https://tripadvisor.in' + tripadvisor_link
					hotel_detail = {'__id' : unique_key,'name' : name, 'prices' : vendors_price, 'rating' : hotel_rating, 'image_link' : image_link, 'hotellink' : add_head_tripadvisor_link}
					details.append(hotel_detail)
				except Exception as e:
					print(e)
		return(details)

	def getrestaurants(self):
		session = HTMLSession()
		base_url = 'https://www.swiggy.com/delhi?page={pageno}'
		link_list = []
		for i in range(1, 8):
			link = base_url.format(pageno = i)
			link_list.append(link)
		detail_list = []
		for links in link_list:
			r = session.get(links)
			soup = BeautifulSoup(r.content, 'html.parser')
			restaurants = soup.find_all('div', attrs = {'class' : '_3XX_A'})
			for restaurant in restaurants:
				details_field = ['name', 'cuisine', 'rating', 'price', 'restaurant_url']
				name = restaurant.find('div', attrs = {'class' : 'nA6kb'}).text
				cuisine = restaurant.find('div', attrs = {'class' : '_1gURR'}).text
				rating = restaurant.find('div', attrs = {'class' : '_9uwBC'}).text
				price = restaurant.find('div', attrs = {'class' : 'nVWSi'}).text
				restaurant_url = restaurant.find('a', attrs = {'class' : '_1j_Yo'})['href']
				restaurant_url = 'https://swiggy.com' + restaurant_url
				detail_dic = {'name' : name, 'cuisine' : cuisine, 'rating' : rating, 'price' : price, 'restaurant_url' : restaurant_url}
				detail_list.append(detail_dic)
		return(detail_list)

	def getthingstosee(self):
		session = HTMLSession()
		r = session.get('https://www.google.com/travel/things-to-do/see-all?g2lb=4675050%2C4605861%2C4371335%2C4306835%2C4624411%2C4644488%2C4401769%2C4317915%2C4640247%2C4270442%2C4596364%2C4258168%2C4649664%2C2503771%2C4597339%2C4419364%2C4641139%2C2503781%2C2502548%2C4291517%2C4270859%2C4284970&hl=en-IN&gl=in&cs=1&ssta=1&dest_mid=%2Fm%2F0dlv0&dest_state_type=sattd&dest_src=ts&q=things%20to%20do%20in%20new%20delhi&sa=X&ved=2ahUKEwjuyfCNyM_0AhUTlNgFHQUzC0EQuL0BegQICBAy#ttdm=28.611263_77.238089_12&ttdmf=%252Fm%252F04w9c2')
		soup = BeautifulSoup(r.content, 'html.parser')
		elements = soup.find_all('div', attrs = {'class' : 'Ld2paf'})
		all_detail = []
		for element in elements:
			details_field = ['name', 'rating', 'description', 'image_link']
			name = element.find('div', attrs = {'class' : 'skFvHc YmWhbc'}).text
			try:
				rating = element.find('div', attrs = {'class' : 'tP34jb'}).text
			except:
				rating = 'Not Available'
			try:
				des = element.find('div', attrs = {'class' : 'nFoFM'}).text
			except:
				des = 'Not Available'
			image_container = element.find('img')
			if image_container:
				image_link =  image_container['data-src']
			else:
				image_link = None
			detail_dic = {'name' : name, 'rating' : rating, 'description' : des, 'image_link' : image_link}
			all_detail.append(detail_dic)
		return(all_detail)


