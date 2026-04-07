const indiaPlaces = [
{ name:"Agra", img:"Taj_Mahal_(Edited).jpeg", desc:"Taj Mahal Wonder of World", fullDescription:"Home to the iconic Taj Mahal, one of the Seven Wonders of the World. This UNESCO World Heritage Site is a masterpiece of Mughal architecture. Best time to visit: October-March. Temperature: 10-30°C. Attractions: Taj Mahal, Agra Fort, Fatehpur Sikri. Best time to visit Taj Mahal is early morning or sunset for stunning photography."},
{ name:"Jaipur", img:"East_facade_Hawa_Mahal_Jaipur_from_ground_level_(July_2022)_-_img_01.jpg", desc:"The Pink City", fullDescription:"Famous for its pink-colored buildings and vibrant culture. Known for its geometric city planning and heritage architecture. Temperature: 15-40°C. Best Season: November-February. Top Attractions: City Palace, Jantar Mantar, Hawa Mahal. Don't miss the local bazaars for traditional crafts and textiles. Rajasthan's capital offers an authentic royal experience."},
{ name:"Goa", img:"BeachFun.jpg", desc:"Beaches & Nightlife", fullDescription:"India's smallest state famous for golden beaches and vibrant nightlife. Portuguese heritage reflected in colonial architecture and churches. Temperature: 24-32°C. Best Season: October-March. Activities: Water sports, beach hopping, nightlife, heritage exploration. Famous beaches: Baga, Calangute, Palolem. Seafood cuisine is world-class here."},
{ name:"Varanasi", img:"Varanasi,_India,_Ghats,_Cremation_ceremony_in_progress.jpg", desc:"Spiritual Capital", fullDescription:"One of the world's oldest continuously inhabited cities and Hinduism's holiest site. Situated on the banks of Ganges River. Temperature: 10-40°C. Best time: October-March. Experiences: Ganga Aarti, boat rides, spiritual exploration. Visit early morning for an authentic spiritual experience. The ancient ghats and temples offer profound cultural insights."},
{ name:"Manali", img:"Manali_City.jpg", desc:"Snow Mountains", fullDescription:"A picturesque hill station nestled in the Himalayas. Perfect for adventure lovers and nature enthusiasts. Temperature: 5-20°C. Best Season: March-October. Activities: Trekking, paragliding, skiing (winter), river rafting, camping. Attractions: Hadimba Temple, Valley of Gods, Old Manali bazaar. Gateway to Spiti Valley and Ladakh."},
{ name:"Shimla", img:"Landscape_of_Shimla_,_Himachal_Pradesh.jpg", desc:"Hill Station", fullDescription:"The Queen of Hill Stations with colonial charm and scenic beauty. Once the summer capital of British India. Temperature: 5-25°C. Best Time: March-June, September-October. Attractions: Kali Bari Temple, Christ Church, Jakhu Temple, Mall Road. Famous for toy train rides and adventure sports. Ideal for family getaways."},
{ name:"Kashmir", img:"Thajiwas_Park,_Sonamarg,_Jammu_and_Kashmir,_India (1).jpg", desc:"Paradise on Earth", fullDescription:"Often called 'Paradise on Earth' with stunning natural beauty. Features Dal Lake, snow-capped mountains, and lush valleys. Temperature: 0-25°C. Best Season: May-September. Activities: Houseboat stays, trekking, skiing, adventure sports. Attractions: Dal Lake, Gulmarg, Pahalgam, Srinagar. Kashmiri handicrafts and cuisine are world-renowned."},
{ name:"Delhi", img:"India_Gate_2014-11-01.jpg", desc:"Capital of India", fullDescription:"The political heart of India with a rich historical legacy spanning centuries. Blend of Old and New Delhi cultures. Temperature: 8-40°C. Best Time: October-March. Must-See: India Gate, Red Fort, Jama Masjid, Qutub Minar, Humayun's Tomb. Street food is amazing here. Perfect base for exploring North India."},
{ name:"Mumbai", img:"Bandra_Worli_Sea-Link_(cropped).jpg", desc:"City of Dreams", fullDescription:"India's financial capital and entertainment hub. Modern skyline meets diverse culture and Bollywood charm. Temperature: 17-32°C. Best Season: October-May. Attractions: Gateway of India, Marine Drive, Bandra Worli Sea Link, Bollywood studios. World-class restaurants, shopping, and nightlife. Home to India's stock exchange and corporate headquarters."},
{ name:"Kerala", img:"Boathouse_(7063399547).jpg", desc:"God's Own Country", fullDescription:"Tropical paradise known for backwaters, beaches, and spices. Highest literacy rate and quality of life in India. Temperature: 20-33°C. Year-round destination. Attractions: Backwater cruises, houseboat stays, beach resorts, tea plantations, ayurveda spas. Famous for coconut, spice, and seafood. Ideal for wellness and relaxation retreats."}
];

const odishaPlaces = [
{ name:"Puri", img:"Shri_Jagannatha_Temple.jpg", desc:"Jagannath Temple", fullDescription:"One of the four sacred pilgrimage sites for Hindus. Home to the magnificent Jagannath Temple with its 65-meter tall tower. The annual Rath Yatra festival attracts millions of pilgrims. Temperature: 15-35°C. Best Season: October-March. Beach seaside location perfect for relaxation. Spiritual significance combined with beautiful coastal scenery."},
{ name:"Konark", img:"Konark_Temple.jpg", desc:"Sun Temple", fullDescription:"A UNESCO World Heritage Site dedicated to the Sun God Surya. Built in 13th century with intricate stone carvings depicting celestial bodies. Temperature: 15-35°C. Best Time: October to March. The temple is designed like a giant chariot with wheels. One of India's greatest architectural achievements. Located near beautiful beaches."},
{ name:"Chilika", img:"Birds_eyeview_of_Chilika_Lake.jpg", desc:"Largest Lagoon", fullDescription:"India's largest coastal lagoon and a wintering ground for migratory birds. Perfect for water sports and bird watching (November-February). Temperature: 15-32°C. Best Season: October-February for bird watching. Home to endangered Irrawaddy dolphins. Sunset boat rides are spectacular. Excellent for photography and nature lovers."},
{ name:"Bhubaneswar", img:"bbsr.jpg", desc:"Temple City", fullDescription:"Odisha's capital known for its 700+ temples reflecting Odia culture. Traditional handicrafts, handloom products, and tribal art flourish here. Temperature: 15-38°C. Best Season: October-March. Attractions: Lingaraj Temple, Odisha State Museum, Nandankanan Zoo. Gateway to exploring Odisha's temples and culture. Perfect blend of tradition and modernity."},
{ name:"Cuttack", img:"Cuttack_Bali_Yatra_Gate.jpg", desc:"Silver City", fullDescription:"Famous for its intricate silver jewelry and handcrafted filigree work. Ancient walled city with a rich trading history. Temperature: 15-38°C. During Bali Yatra (November), the city celebrates its maritime trading heritage. Excellent shopping destination for silver ornaments. Street food is delicious. Unique blend of history and commerce."},
{ name:"Daringbadi", img:"Lover's_point,_Daringbadi.jpg", desc:"Kashmir of Odisha", fullDescription:"A scenic hill station with rolling green hills and coffee plantations. Cooler climate compared to coastal Odisha. Temperature: 8-25°C. Best Season: November-January. Activities: Trekking, village tours, coffee plantation visits, bird watching. Attractions: Lover's Point, Belghar Waterfall. Perfect for honeymooners and nature enthusiasts."},
{ name:"Gopalpur", img:"Gopalpur_'s_beach,_the_ocean.jpeg", desc:"Sea Beach", fullDescription:"A serene beach destination with laid-back atmosphere and clean sandy shores. Less crowded compared to other Indian beaches. Temperature: 20-32°C. Year-round destination. Activities: Swimming, surfing, beach walks, seafood dining. Watch fishermen's traditional boats in the morning. Ideal for a peaceful beach getaway."},
{ name:"Simlipal", img:"Tiger_at_Similipal_Forest.png", desc:"Tiger Reserve", fullDescription:"A pristine wildlife sanctuary in the Mayurbhanj district teeming with Bengal tigers, elephants, and wild boars. Dense forests and beautiful waterfalls. Temperature: 10-30°C. Best Season: June-October for waterfalls, November-March for wildlife. Activities: Jungle trekking, wildlife spotting, waterfall visits. Home to diverse flora and fauna. Paradise for wildlife photographers."},
{ name:"Hirakud", img:"Hirakud_Dam_Panorama.jpg", desc:"Longest Dam", fullDescription:"The longest earth dam in the world stretching 26 km across the Mahanadi river. Offers stunning views and picnic spots. Temperature: 15-38°C. Best Season: October to March. Activities: Dam walks, boat rides, island visits, photography. The reservoir creates beautiful islands. Great for family picnics and nature lovers."},
{ name:"Rourkela", img:"Suraksha_Path_Bridge_near_IG_Park_Rourkela.jpg", desc:"Steel City", fullDescription:"An industrial city in northern Odisha, modern city with planned infrastructure. Home to famous steel plants. Temperature: 10-40°C. Best Season: October-March. Attractions: IG Park, Mandira Dam, Japanese Garden, tribal culture experiences. Blend of industrial development and green spaces. Worth visiting for industrial tourism."},
{name:"koraput",img:"Table_mountain_Koraput.jpg", desc:"Nature's Paradise", fullDescription:"A scenic tribal district surrounded by mountains, forests, and agricultural fields. Pristine natural beauty with minimal tourism. Temperature: 8-28°C. Best Season: October-February. Activities: Hiking, village tours, tribal art exploration, waterfall visits. Meeting point of three hill ranges. Perfect for adventure seekers and nature purists seeking untouched wilderness."}
];

const globalPlaces = [
{ name:"Great Wall of China", img:"great_wall_china.jpg", desc:"Ancient Wonder", fullDescription:"One of the Seven Wonders of the World, stretching over 13,000 miles across northern China. Built over centuries to protect against invasions. Temperature: -10°C to 30°C. Best Season: April-June, September-October. Activities: Hiking, photography, cable car rides. UNESCO World Heritage Site. Offers stunning views and historical significance. A must-visit for history enthusiasts."},
{ name:"The Louvre Museum", img:"louvre_paris.jpg", desc:"Art Masterpieces", fullDescription:"Home to the Mona Lisa and thousands of other priceless artworks. World's largest art museum in Paris, France. Temperature: 5-25°C. Best Season: April-June, September-October. Attractions: Mona Lisa, Venus de Milo, Winged Victory. Extensive collections from ancient to modern art. Plan for several hours to explore properly."},
{ name:"Colosseum", img:"colosseum_rome.jpg", desc:"Roman Amphitheater", fullDescription:"Iconic ancient Roman amphitheater in Rome, Italy. Could seat 50,000 spectators for gladiatorial contests. Temperature: 10-30°C. Best Season: April-June, September-October. UNESCO site. Evening shows with lighting create magical atmosphere. Symbol of ancient Roman engineering and entertainment."},
{ name:"Machu Picchu", img:"machu_picchu.jpg", desc:"Lost City", fullDescription:"Ancient Incan citadel high in the Andes Mountains of Peru. Built in the 15th century, abandoned and rediscovered in 1911. Temperature: 5-20°C. Best Season: May-September (dry season). Activities: Hiking Inca Trail, exploring ruins. UNESCO World Heritage Site. Surrounded by stunning mountain scenery."},
{ name:"Eiffel Tower", img:"eiffel_tower.jpg", desc:"Paris Icon", fullDescription:"Iconic iron lattice tower in Paris, France. Built for 1889 World's Fair, symbol of French engineering. Temperature: 5-25°C. Best Season: April-June, September-October. Activities: Elevator ride to top, Seine River cruises. Stunning city views, especially at night when illuminated. Perfect for romantic photos."},
{ name:"Statue of Liberty", img:"statue_liberty.jpg", desc:"Freedom Symbol", fullDescription:"Massive neoclassical sculpture on Liberty Island, New York Harbor. Gift from France symbolizing freedom and democracy. Temperature: 0-25°C. Best Season: April-June, September-October. Activities: Ferry ride, museum visit, crown access. Represents American ideals. Iconic skyline views of Manhattan."},
{ name:"Sydney Opera House", img:"sydney_opera.jpg", desc:"Architectural Marvel", fullDescription:"Modernist performing arts center in Sydney, Australia. Designed by Danish architect Jørn Utzon, opened in 1973. Temperature: 15-25°C. Best Season: September-November, March-May. Activities: Opera/ballet shows, harbor cruises, tours. UNESCO World Heritage Site. Iconic sail-like design."},
{ name:"Sagrada Familia", img:"sagrada_familia.jpg", desc:"Gaudi's Masterpiece", fullDescription:"Massive Roman Catholic church in Barcelona, Spain. Antoni Gaudí's unfinished masterpiece, construction began in 1882. Temperature: 10-25°C. Best Season: April-June, September-October. Activities: Guided tours, climbing towers. Unique Gothic and Art Nouveau architecture. Still under construction after 140+ years."},
{ name:"Angkor Wat", img:"angkor_wat.jpg", desc:"Ancient Temple", fullDescription:"Largest religious monument in the world, located in Cambodia. Built in 12th century as Hindu temple, later Buddhist. Temperature: 25-35°C. Best Season: November-March (dry season). Activities: Temple exploration, sunrise viewing. UNESCO site. Intricate stone carvings and bas-reliefs depict Hindu mythology."},
{ name:"Pyramids of Giza", img:"pyramids_giza.jpg", desc:"Ancient Tombs", fullDescription:"Ancient pyramid complex in Egypt including Great Pyramid of Khufu. Built around 2580-2565 BC as royal tombs. Temperature: 15-35°C. Best Season: October-April. Activities: Camel rides, Sphinx viewing. Only surviving Ancient World Wonder. Engineering marvel of ancient Egypt."},
{ name:"Burj Khalifa", img:"burj_khalifa.jpg", desc:"World's Tallest", fullDescription:"Tallest man-made structure at 828 meters in Dubai, UAE. Mixed-use skyscraper with observation decks and luxury amenities. Temperature: 20-40°C. Best Season: November-March. Activities: Observation deck visits, luxury shopping. Modern architectural wonder. Stunning desert and city views."},
{ name:"Times Square", img:"times_square.jpg", desc:"City Crossroads", fullDescription:"Major commercial intersection in Midtown Manhattan, New York City. Known for bright lights, billboards, and Broadway theaters. Temperature: 0-25°C. Best Season: April-June, September-October. Activities: Street performances, shopping, theater shows. The 'Crossroads of the World' never sleeps. Iconic urban experience."},
{ name:"Niagara Falls", img:"niagara_falls.jpg", desc:"Natural Wonder", fullDescription:"Massive waterfall system on US-Canada border. Three waterfalls: American, Bridal Veil, and Canadian (Horseshoe). Temperature: -5°C to 25°C. Best Season: May-October. Activities: Boat tours, helicopter rides, hiking. One of world's most powerful waterfalls. Spectacular at night with colored lights."},
{ name:"Grand Canyon", img:"grand_canyon.jpg", desc:"Natural Monument", fullDescription:"Immense canyon carved by Colorado River in Arizona, USA. Over 277 miles long, up to 18 miles wide, mile deep. Temperature: 0-30°C. Best Season: March-May, September-October. Activities: Hiking, rafting, helicopter tours. UNESCO World Heritage Site. Stunning geological formations and desert landscapes."},
{ name:"Venice Canals", img:"venice_canals.jpg", desc:"Floating City", fullDescription:"Unique city built on 118 islands in Venetian Lagoon, Italy. Connected by 400+ bridges and canals instead of roads. Temperature: 5-25°C. Best Season: April-June, September-October. Activities: Gondola rides, St. Mark's Square, Basilica visits. Romantic atmosphere with historic architecture. No cars allowed."},
{ name:"Santorini", img:"santorini.jpg", desc:"Aegean Paradise", fullDescription:"Volcanic Greek island in Aegean Sea famous for white-washed buildings and stunning sunsets. Part of Cyclades archipelago. Temperature: 15-25°C. Best Season: April-June, September-October. Activities: Beach relaxation, wine tasting, caldera views. Picturesque blue-domed churches. Perfect for honeymooners and photographers."},
{ name:"Petra", img:"petra.jpg", desc:"Rose City", fullDescription:"Ancient city carved into rose-red cliffs in Jordan. Capital of Nabataean Kingdom, UNESCO World Heritage Site. Temperature: 10-30°C. Best Season: March-May, September-October. Activities: Camel rides, hiking, exploring tombs. Featured in Indiana Jones. Architectural marvel of ancient engineering."},
{ name:"Mount Fuji", img:"mount_fuji.jpg", desc:"Sacred Mountain", fullDescription:"Active stratovolcano and Japan's highest peak at 3,776 meters. Considered sacred in Shinto religion and Japanese culture. Temperature: -10°C to 20°C. Best Season: July-August (climbing), all year for viewing. Activities: Hiking, hot springs, lake tours. Symbol of Japan. Stunning views from surrounding areas."},
{ name:"Big Ben", img:"big_ben.jpg", desc:"London Icon", fullDescription:"Famous clock tower in London, England, part of Palace of Westminster. Houses Great Bell weighing 13.5 tons. Temperature: 5-20°C. Best Season: April-June, September-October. Activities: River cruises, palace tours. Historic landmark. Chimes heard worldwide. Symbol of British parliamentary democracy."},
{ name:"Christ the Redeemer", img:"christ_redeemer.jpg", desc:"Rio Landmark", fullDescription:"Massive Art Deco statue of Jesus Christ in Rio de Janeiro, Brazil. Stands 98 feet tall on Corcovado Mountain. Temperature: 20-30°C. Best Season: March-May, September-November. Activities: Cable car rides, city views. UNESCO site. One of New Seven Wonders. Visible from most of Rio."}
];

/* ========= RENDER PLACES UI ========= */
function renderPlaces(places, containerId) {
    const container = document.getElementById(containerId);
    container.innerHTML = "";
    
    places.forEach(place => {
        const card = document.createElement("div");
        card.className = "place-card";
        card.innerHTML = `
            <img src="static/images/${place.img}" alt="${place.name}">
            <div class="place-info">
                <h3>${place.name}</h3>
                <p>${place.desc}</p>
            </div>
        `;
        
        // Add click event to show details
        card.addEventListener("click", () => showPlaceDetails(place, card));
        container.appendChild(card);
    });
}

/* ========= SHOW PLACE DETAILS ========= */
function showPlaceDetails(place, cardElement) {
    // Update title
    document.getElementById("detail-title").textContent = place.name;
    
    // Update image
    const detailImage = document.getElementById("detail-image");
    detailImage.src = `static/images/${place.img}`;
    detailImage.style.display = "block";
    
    // Update description
    document.getElementById("detail-description").innerHTML = `
        <p><strong>${place.desc}</strong></p>
        <p>${place.fullDescription || "Discover the beauty and charm of this wonderful destination. Experience the culture, history, and attractions that make this place special."}</p>
    `;
    
    // Remove active class from all cards
    document.querySelectorAll(".place-card").forEach(c => c.classList.remove("active"));
    
    // Add active class to clicked card
    cardElement.classList.add("active");
}

document.addEventListener("DOMContentLoaded", () => {
    renderPlaces(indiaPlaces, "india-container");
    renderPlaces(odishaPlaces, "odisha-container");
    renderPlaces(globalPlaces, "global-container");
});
