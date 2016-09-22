### eleme

1. shopinfo

    1. request

            http://www.ele.me/restapi/v4/restaurants/725427/?extras%5B%5D=statistics&extras%5B%5D=certification&extras%5B%5D=license&extras%5B%5D=identification&extras%5B%5D=album

    1. response

            {
              "id": 725427,
              "name": "百萨屋",
              "latitude": 89.1,
              "longitude": 179.1,
              "description": "本店经济实惠，欢迎品尝。",
              "phone": "67877260",
              "order_mode": 9,
              "promotion_info": "为了你能及时用餐，请您提前50分钟下单。",
              "name_for_url": "yzbsw",
              "flavors": "",
              "is_time_ensure": false,
              "is_premium": false,
              "time_ensure_full_description": "",
              "recent_order_num": 12,
              "rating": 0,
              "float_minimum_order_amount": null,
              "float_delivery_fee": 0,
              "bidding": null,
              "image_path": "/a/3d/9606c16a0d185dbe737208c555f40jpeg.jpeg",
              "is_free_delivery": true,
              "minimum_order_amount": 30,
              "order_lead_time": 43,
              "is_support_invoice": false,
              "is_new": false,
              "is_third_party_delivery": false,
              "is_in_book_time": true,
              "rating_count": 3,
              "address": "北京市北京经济技术开发区天华园一里一区5号楼一层13轴至14轴",
              "month_sales": 39,
              "delivery_fee": 0,
              "minimum_free_delivery_amount": 0,
              "minimum_order_description": "",
              "minimum_invoice_amount": 0,
              "is_open_time": true,
              "opening_hours": [
                "09:00/21:00"
              ],
              "book_times": [
                "18:00:00",
                "18:15:00",
                "18:30:00",
                "18:45:00",
                "19:00:00",
                "19:15:00",
                "19:30:00",
                "19:45:00",
                "20:00:00",
                "20:15:00",
                "20:30:00",
                "20:45:00"
              ],
              "is_online_payment": true,
              "status": 1,
              "distance": null,
              "supports": [
                {
                  "id": 3,
                  "name": "在线支付",
                  "description": "可使用支付宝、微信、手机QQ进行在线支付",
                  "icon_color": "FF4E00",
                  "icon_name": "付"
                }
              ],
              "food_tips": "(3) 月售39份",
              "restaurant_tips": "30元起送 / 43分钟 / ",
              "next_business_time": "",
              "is_coupon_enabled": false,
              "is_insurance": false,
              "delivery_mode": null,
              "business_district": "",
              "only_use_poi": true,
              "closing_count_down": 0,
              "certification": {
                "restaurant_id": 725427,
                "person_name": "",
                "identity_card_no": "",
                "identity_card_image_front": "",
                "identity_card_image_front_wm": "",
                "identity_card_image_back": "",
                "identity_card_image_back_wm": "",
                "health_card_image_front": "",
                "health_card_image_front_wm": "",
                "health_card_image_back": "",
                "health_card_image_back_wm": "",
                "corp_name": "北京亦品客披萨饼店",
                "license_no": "",
                "license_location": "北京市北京经济技术开发区天华园一里一区5号楼一层13轴至14轴",
                "license_expire_date": "",
                "license_image": "e6bd25cd4c7b17dac7cc7e3bd1591699jpeg",
                "license_image_wm": "f1e1f9915b4c190bd2fa77bf37c8f771jpeg",
                "restaurant_service_license_copy": "6326eb3d5b5d26627788c99c84cd9cfcjpeg",
                "restaurant_service_license_copy_wm": "8e08ac1b01ccb09e24f930c6ddab0398jpeg",
                "type": 2,
                "status": 1,
                "comment": "",
                "created_at": 1458628163,
                "updated_at": 1458628164
              },
              "statistics": null,
              "license": {},
              "identification": null,
              "album": [
                {
                  "name": "门面",
                  "cover_image_hash": "/1/41/5a598077e27dfef8f1714be9e41dbjpeg.jpeg",
                  "photos": [
                    {
                      "id": 1843661,
                      "image_hash": "/1/41/5a598077e27dfef8f1714be9e41dbjpeg.jpeg",
                      "description": "",
                      "type": "FRONT"
                    }
                  ],
                  "count": 1
                },
                {
                  "name": "大堂",
                  "cover_image_hash": "/8/b4/03fb9ba2b6e31b495dbf4dca0a3f7jpeg.jpeg",
                  "photos": [
                    {
                      "id": 1843666,
                      "image_hash": "/8/b4/03fb9ba2b6e31b495dbf4dca0a3f7jpeg.jpeg",
                      "description": "",
                      "type": "HALL"
                    }
                  ],
                  "count": 1
                },
                {
                  "name": "后厨",
                  "cover_image_hash": "/0/9d/dbc4196799cc39a9d96f8dbfbe97cjpeg.jpeg",
                  "photos": [
                    {
                      "id": 1843672,
                      "image_hash": "/0/9d/dbc4196799cc39a9d96f8dbfbe97cjpeg.jpeg",
                      "description": "",
                      "type": "KITCHEN"
                    }
                  ],
                  "count": 1
                }
              ]
            }

1. food info

    1. request

            http://www.ele.me/restapi/v4/restaurants/725427/mutimenu

    1. response

            [
              {
                "description": "",
                "is_selected": true,
                "icon_url": "",
                "foods": [
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375488,
                    "image_path": "http://fuss10.elemecdn.com/f/3c/2987f0e4c1367d604f683bb81d971jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "huangjiashengyan",
                    "name": "皇家盛宴",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65811244,
                        "name": "皇家盛宴-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiashengyan-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65811245,
                        "name": "皇家盛宴-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiashengyan-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 91.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 65811246,
                        "name": "皇家盛宴-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiashengyan-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 129.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375488,
                    "image_path": "http://fuss10.elemecdn.com/3/e8/9be57d14f2a4a1b4ad1252b19ef7ejpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "huangjiahaixian",
                    "name": "皇家海鲜",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65821232,
                        "name": "皇家海鲜-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiahaixian-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 65.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 65821235,
                        "name": "皇家海鲜-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiahaixian-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 91.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65821237,
                        "name": "皇家海鲜-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiahaixian-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 129.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375488,
                    "image_path": "http://fuss10.elemecdn.com/7/04/e5ab70ea5a0a0fc75b8293c7c2e9ajpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "huangjiamoxigelaxia",
                    "name": "皇家墨西哥辣虾",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65822395,
                        "name": "皇家墨西哥辣虾-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiamoxigelaxia-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 58.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65822396,
                        "name": "皇家墨西哥辣虾-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiamoxigelaxia-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 83.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65822397,
                        "name": "皇家墨西哥辣虾-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiamoxigelaxia-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 119.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375488,
                    "image_path": "http://fuss10.elemecdn.com/4/ec/8486558f1d27d9e422060104f9fadjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "huangjiaqingxinshujiao",
                    "name": "皇家清馨薯角",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65822793,
                        "name": "皇家清馨薯角-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiaqingxinshujiao-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65822794,
                        "name": "皇家清馨薯角-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiaqingxinshujiao-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 91.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65823229,
                        "name": "皇家清馨薯角-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiaqingxinshujiao-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 129.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375488,
                    "image_path": "http://fuss10.elemecdn.com/1/7e/303c524da6b44da36ac6c40576181jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "huangjiatianyuan",
                    "name": "皇家田园",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65824477,
                        "name": "皇家田园-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiatianyuan-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 53.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65824479,
                        "name": "皇家田园-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiatianyuan-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 77.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65824480,
                        "name": "皇家田园-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "huangjiatianyuan-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 108.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  }
                ],
                "activity": null,
                "is_activity": false,
                "id": 6375488,
                "name": "皇家系列比萨"
              },
              {
                "description": "",
                "is_selected": false,
                "icon_url": "",
                "foods": [
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/3/89/d69ce6a7ba68d065f5fad7d3cb69fjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiaweiyi",
                    "name": "夏威夷",
                    "month_sales": 2,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65826288,
                        "name": "夏威夷-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiaweiyi-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 2,
                        "price": 39.0,
                        "stock": 9997
                      },
                      {
                        "original_price": null,
                        "food_id": 65826289,
                        "name": "夏威夷-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiaweiyi-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 61.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65826291,
                        "name": "夏威夷-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiaweiyi-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 92.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售2份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 5.0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/a/16/26339080dbe70f97895688ce210cejpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "papaluoni",
                    "name": "帕帕罗尼",
                    "month_sales": 2,
                    "satisfy_count": 1,
                    "rating_count": 1,
                    "activity": null,
                    "satisfy_rate": 100,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65827075,
                        "name": "帕帕罗尼-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "papaluoni-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 61.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65827079,
                        "name": "帕帕罗尼-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "papaluoni-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 92.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65827060,
                        "name": "帕帕罗尼-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "papaluoni-9cun",
                        "recent_rating": 5.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 2,
                        "price": 39.0,
                        "stock": 9998
                      }
                    ],
                    "tips": "1评价 月售2份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/6/89/8dfa87b9f55f069d14c97d2fd4b3ejpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "heijiaoniurou",
                    "name": "黑椒牛肉",
                    "month_sales": 2,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65827465,
                        "name": "黑椒牛肉-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "heijiaoniurou-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 2,
                        "price": 39.0,
                        "stock": 9997
                      },
                      {
                        "original_price": null,
                        "food_id": 65827467,
                        "name": "黑椒牛肉-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "heijiaoniurou-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 61.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65827468,
                        "name": "黑椒牛肉-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "heijiaoniurou-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 92.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售2份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/0/53/bbff686e0330de84295db71b0cffajpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "bocaipeigen",
                    "name": "菠菜培根",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65878430,
                        "name": "菠菜培根-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "bocaipeigen-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 39.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65878432,
                        "name": "菠菜培根-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "bocaipeigen-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 61.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65878433,
                        "name": "菠菜培根-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "bocaipeigen-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 92.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/8/a5/4ebe6a94e4106991ef44123cf8603jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "moxigelaxia",
                    "name": "墨西哥辣虾",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65878870,
                        "name": "墨西哥辣虾-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "moxigelaxia-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 43.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65878873,
                        "name": "墨西哥辣虾-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "moxigelaxia-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 65.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 65878875,
                        "name": "墨西哥辣虾-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "moxigelaxia-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 97.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/a/e6/d1ac6276405f082313707c999658djpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "tesealabo",
                    "name": "特色阿拉伯",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65881416,
                        "name": "特色阿拉伯-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesealabo-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 43.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 65881417,
                        "name": "特色阿拉伯-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesealabo-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65881418,
                        "name": "特色阿拉伯-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesealabo-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 97.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/2/ee/661fcabcc62a8cdc9fd8cac3d9341jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "tesezhaoshaoji",
                    "name": "特色照烧鸡",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65882048,
                        "name": "特色照烧鸡-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesezhaoshaoji-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 43.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 65882050,
                        "name": "特色照烧鸡-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesezhaoshaoji-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65882052,
                        "name": "特色照烧鸡-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesezhaoshaoji-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 97.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/4/d8/6b103bcaf632601be1346a6d9e18cjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "changxiangyi",
                    "name": "肠相依",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65882819,
                        "name": "肠相依-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "changxiangyi-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 43.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 65882820,
                        "name": "肠相依-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "changxiangyi-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65882822,
                        "name": "肠相依-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "changxiangyi-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 97.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/0/fe/dfcbed87cfcda3edf15405430f4aajpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "jiduxianghun",
                    "name": "极度香荤",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65883496,
                        "name": "极度香荤-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "jiduxianghun-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 43.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65883497,
                        "name": "极度香荤-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "jiduxianghun-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65883499,
                        "name": "极度香荤-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "jiduxianghun-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 97.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/d/66/8bf4fc66e823adc9345e211f774b8jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiabingxiejiang",
                    "name": "虾兵蟹将",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65884617,
                        "name": "虾兵蟹将-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiabingxiejiang-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65884619,
                        "name": "虾兵蟹将-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiabingxiejiang-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 73.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65884622,
                        "name": "虾兵蟹将-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiabingxiejiang-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 102.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/d/c9/42fc01ae4549b651931f602aea5f8jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "qingxinshujiaobisa",
                    "name": "清馨薯角比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65885726,
                        "name": "清馨薯角比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "qingxinshujiaobisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65885728,
                        "name": "清馨薯角比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "qingxinshujiaobisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 73.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65885730,
                        "name": "清馨薯角比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "qingxinshujiaobisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 102.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/8/03/f02770499fadd14330fa1ca0b5eb5jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "haidijinqiangyubisa",
                    "name": "海底金枪鱼比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65886531,
                        "name": "海底金枪鱼比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "haidijinqiangyubisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65886532,
                        "name": "海底金枪鱼比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "haidijinqiangyubisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 73.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65886533,
                        "name": "海底金枪鱼比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "haidijinqiangyubisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 102.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/7/ec/b043fc635ba444457e77adf951028jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "baisazhizunbisa",
                    "name": "百萨至尊比萨",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65887001,
                        "name": "百萨至尊比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "baisazhizunbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 51.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 65887005,
                        "name": "百萨至尊比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "baisazhizunbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 73.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65887007,
                        "name": "百萨至尊比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "baisazhizunbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 102.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/f/24/23586927e3492bb31251c3e31594fjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiangmangkalijibisa",
                    "name": "香芒咖喱鸡比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65888173,
                        "name": "香芒咖喱鸡比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiangmangkalijibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65888174,
                        "name": "香芒咖喱鸡比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiangmangkalijibisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 73.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65888175,
                        "name": "香芒咖喱鸡比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiangmangkalijibisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 102.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/2/24/2b3c0c6065aba887bda0fb1adc5aajpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiandanchaorenbisa",
                    "name": "咸蛋超人比萨",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65889454,
                        "name": "咸蛋超人比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiandanchaorenbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 51.0,
                        "stock": 9997
                      },
                      {
                        "original_price": null,
                        "food_id": 65889456,
                        "name": "咸蛋超人比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiandanchaorenbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 73.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65889457,
                        "name": "咸蛋超人比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiandanchaorenbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 102.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": "http://fuss10.elemecdn.com/c/e1/277cdc89e7888256c03a060bc47f9jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "shizhenhuibisa",
                    "name": "十珍汇比萨",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65889975,
                        "name": "十珍汇比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shizhenhuibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 43.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 65889976,
                        "name": "十珍汇比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shizhenhuibisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65889977,
                        "name": "十珍汇比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shizhenhuibisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 97.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "mingmeitianyuan",
                    "name": "明媚田园",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65878067,
                        "name": "明媚田园-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "mingmeitianyuan-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 39.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65878068,
                        "name": "明媚田园-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "mingmeitianyuan-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 61.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65878069,
                        "name": "明媚田园-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "mingmeitianyuan-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 92.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "niurouwanbisa",
                    "name": "牛肉丸比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65891225,
                        "name": "牛肉丸比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "niurouwanbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65891226,
                        "name": "牛肉丸比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "niurouwanbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 73.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65891227,
                        "name": "牛肉丸比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "niurouwanbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 102.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "shuiguobisa",
                    "name": "水果比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65891634,
                        "name": "水果比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shuiguobisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65891635,
                        "name": "水果比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shuiguobisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 73.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65891636,
                        "name": "水果比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shuiguobisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 102.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 5.0,
                    "limitation": {},
                    "category_id": 6375507,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "liumangbisa",
                    "name": "榴芒比萨",
                    "month_sales": 1,
                    "satisfy_count": 1,
                    "rating_count": 1,
                    "activity": null,
                    "satisfy_rate": 100,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65892140,
                        "name": "榴芒比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "liumangbisa-9cun",
                        "recent_rating": 5.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 86.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 65892141,
                        "name": "榴芒比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "liumangbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 108.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65892142,
                        "name": "榴芒比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "liumangbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 136.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "1评价 月售1份",
                    "attributes": [],
                    "description": ""
                  }
                ],
                "activity": null,
                "is_activity": false,
                "id": 6375507,
                "name": "纽约系列比萨"
              },
              {
                "description": "",
                "is_selected": false,
                "icon_url": "",
                "foods": [
                  {
                    "rating": 5.0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/9/10/0a644970dd50ac1a2481d6316bed5jpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiaweiyibisa-9cun",
                    "name": "夏威夷比萨-9寸",
                    "month_sales": 2,
                    "satisfy_count": 1,
                    "rating_count": 1,
                    "activity": null,
                    "satisfy_rate": 100,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65977765,
                        "name": "夏威夷比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiaweiyibisa-9cun",
                        "recent_rating": 5.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 2,
                        "price": 53.0,
                        "stock": 9997
                      }
                    ],
                    "tips": "1评价 月售2份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/9/10/0a644970dd50ac1a2481d6316bed5jpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiaweiyibisa-11cun",
                    "name": "夏威夷比萨-11寸",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65977766,
                        "name": "夏威夷比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiaweiyibisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 77.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/9/10/0a644970dd50ac1a2481d6316bed5jpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiaweiyibisa-13cun",
                    "name": "夏威夷比萨-13寸",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65977767,
                        "name": "夏威夷比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiaweiyibisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 113.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/7/51/75e48438bc7968ba59bb7c2fcbe42jpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "papaluonibisa-9cun",
                    "name": "帕帕罗尼比萨-9寸",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65978125,
                        "name": "帕帕罗尼比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "papaluonibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 53.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/7/51/75e48438bc7968ba59bb7c2fcbe42jpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "papaluonibisa-11cun",
                    "name": "帕帕罗尼比萨-11寸",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65978126,
                        "name": "帕帕罗尼比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "papaluonibisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 77.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/7/51/75e48438bc7968ba59bb7c2fcbe42jpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "papaluonibisa-13cun",
                    "name": "帕帕罗尼比萨-13寸",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65978127,
                        "name": "帕帕罗尼比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "papaluonibisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 113.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/1/9b/444b93d855af416864d4151df7103jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "heijiaoniuroubisa",
                    "name": "黑椒牛肉比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65978607,
                        "name": "黑椒牛肉比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "heijiaoniuroubisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 53.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65978608,
                        "name": "黑椒牛肉比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "heijiaoniuroubisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 77.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65978609,
                        "name": "黑椒牛肉比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "heijiaoniuroubisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 113.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/a/19/d79e0e4f8025be30336fda93aa14bjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "bocaipeigenbisa",
                    "name": "菠菜培根比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65991602,
                        "name": "菠菜培根比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "bocaipeigenbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 53.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65991604,
                        "name": "菠菜培根比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "bocaipeigenbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 77.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65991605,
                        "name": "菠菜培根比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "bocaipeigenbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 113.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/7/c1/025b0eed395b48d9c8b62729a2043jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "moxigelaxiabisa",
                    "name": "墨西哥辣虾比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65991980,
                        "name": "墨西哥辣虾比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "moxigelaxiabisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 59.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65991981,
                        "name": "墨西哥辣虾比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "moxigelaxiabisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 83.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65991982,
                        "name": "墨西哥辣虾比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "moxigelaxiabisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 119.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/f/96/55137bf1b195a7a349a7f2a3ccb62jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "tesealabobisa",
                    "name": "特色阿拉伯比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65992344,
                        "name": "特色阿拉伯比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesealabobisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 59.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65992345,
                        "name": "特色阿拉伯比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesealabobisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 83.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65992346,
                        "name": "特色阿拉伯比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesealabobisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 119.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/e/a2/0e762815652b3e0ec29f80e0b65fcjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "tesezhaoshaojibisa",
                    "name": "特色照烧鸡比萨",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65992636,
                        "name": "特色照烧鸡比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesezhaoshaojibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 59.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 65992638,
                        "name": "特色照烧鸡比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesezhaoshaojibisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 83.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65992639,
                        "name": "特色照烧鸡比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesezhaoshaojibisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 119.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/7/6f/e5e00f8051e5aac00fd703eaf765djpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "changxiangyibisa",
                    "name": "肠相依比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65993353,
                        "name": "肠相依比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "changxiangyibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 59.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65993354,
                        "name": "肠相依比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "changxiangyibisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 83.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65993355,
                        "name": "肠相依比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "changxiangyibisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 119.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/6/f4/27bbc6e3b62c6a40cbde87ca0a6b5jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "jiduxianghunbisa",
                    "name": "极度香荤比萨",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66002139,
                        "name": "极度香荤比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "jiduxianghunbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 59.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 66002140,
                        "name": "极度香荤比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "jiduxianghunbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 83.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66002141,
                        "name": "极度香荤比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "jiduxianghunbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 119.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/2/de/3a0f879dc3b3ae53869f0d3d8a22djpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "shizhenhuibisa",
                    "name": "十珍汇比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66015867,
                        "name": "十珍汇比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shizhenhuibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 59.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66015868,
                        "name": "十珍汇比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shizhenhuibisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 83.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66015869,
                        "name": "十珍汇比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shizhenhuibisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 119.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/e/3c/f39af608ec0a6e81be8b6f6bbd505jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiabingxiejiangbisa",
                    "name": "虾兵蟹将比萨",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66016141,
                        "name": "虾兵蟹将比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiabingxiejiangbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 65.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 66016143,
                        "name": "虾兵蟹将比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiabingxiejiangbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 91.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66016144,
                        "name": "虾兵蟹将比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiabingxiejiangbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 129.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/c/37/a580b755dc4fc0fab90b795cb148djpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "qingxinshujiaobisa",
                    "name": "清馨薯角比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66016456,
                        "name": "清馨薯角比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "qingxinshujiaobisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66016457,
                        "name": "清馨薯角比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "qingxinshujiaobisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 91.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66016458,
                        "name": "清馨薯角比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "qingxinshujiaobisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 129.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/d/45/57648f50ae28f1294b24c83f3622bjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "haidijinqiangyubisa",
                    "name": "海底金枪鱼比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66016861,
                        "name": "海底金枪鱼比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "haidijinqiangyubisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66016863,
                        "name": "海底金枪鱼比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "haidijinqiangyubisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 91.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66016864,
                        "name": "海底金枪鱼比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "haidijinqiangyubisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 129.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/c/64/f5913b7813af2240d2bd35f024c37jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "baisazhizunbisa",
                    "name": "百萨至尊比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66017370,
                        "name": "百萨至尊比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "baisazhizunbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66017372,
                        "name": "百萨至尊比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "baisazhizunbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 91.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66017374,
                        "name": "百萨至尊比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "baisazhizunbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 129.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/5/aa/3c62ad92cd5508db8ec016eac59a4jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiangmangkalijibisa",
                    "name": "香芒咖喱鸡比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66017660,
                        "name": "香芒咖喱鸡比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiangmangkalijibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66017663,
                        "name": "香芒咖喱鸡比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiangmangkalijibisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 91.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66017664,
                        "name": "香芒咖喱鸡比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiangmangkalijibisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 129.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": "http://fuss10.elemecdn.com/7/49/21a34055c7ed90c4496634a75ff8fjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiandanchaorenbisa",
                    "name": "咸蛋超人比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66018016,
                        "name": "咸蛋超人比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiandanchaorenbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66018017,
                        "name": "咸蛋超人比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiandanchaorenbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 91.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66018018,
                        "name": "咸蛋超人比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiandanchaorenbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 129.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "mingmeitianyuanbisa",
                    "name": "明媚田园比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 65990683,
                        "name": "明媚田园比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "mingmeitianyuanbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 53.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65990684,
                        "name": "明媚田园比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "mingmeitianyuanbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 77.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 65990685,
                        "name": "明媚田园比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "mingmeitianyuanbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 113.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "niurouwanbisa",
                    "name": "牛肉丸比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66018607,
                        "name": "牛肉丸比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "niurouwanbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66018608,
                        "name": "牛肉丸比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "niurouwanbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 91.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66018609,
                        "name": "牛肉丸比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "niurouwanbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 129.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "shuiguobisa",
                    "name": "水果比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66019087,
                        "name": "水果比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shuiguobisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 65.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66019088,
                        "name": "水果比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shuiguobisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 91.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66019089,
                        "name": "水果比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shuiguobisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 129.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376178,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "9寸",
                          "11寸",
                          "13寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "liumangbisa",
                    "name": "榴芒比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66019634,
                        "name": "榴芒比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "liumangbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 98.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66019635,
                        "name": "榴芒比萨-11寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "liumangbisa-11cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "11寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 126.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66019636,
                        "name": "榴芒比萨-13寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "liumangbisa-13cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "13寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 158.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  }
                ],
                "activity": null,
                "is_activity": false,
                "id": 6376178,
                "name": "香芝系列比萨"
              },
              {
                "description": "",
                "is_selected": false,
                "icon_url": "",
                "foods": [
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/7/43/57b01dcb6597e44666172b716ab2ejpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiaweiyibisa",
                    "name": "夏威夷比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66020040,
                        "name": "夏威夷比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiaweiyibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 39.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/2/24/321637740e6be1bd4ae49f327e6f3jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "papaluonibisa",
                    "name": "帕帕罗尼比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66020225,
                        "name": "帕帕罗尼比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "papaluonibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 39.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/4/58/9d50d181165c626b5a286358c6323jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "heijiaoniuroubisa",
                    "name": "黑椒牛肉比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66020427,
                        "name": "黑椒牛肉比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "heijiaoniuroubisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 39.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/0/c9/0a451de726d9b12d04304a8099f7cjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "bocaipeigenbisa",
                    "name": "菠菜培根比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66020713,
                        "name": "菠菜培根比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "bocaipeigenbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 39.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/c/5b/4eb5cc472b9789b5f70cca5b79448jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "moxigelaxiabisa",
                    "name": "墨西哥辣虾比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66020885,
                        "name": "墨西哥辣虾比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "moxigelaxiabisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 43.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/7/1d/e33ad5b8f133ae49cfcafb2d9e655jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "tesealabobisa",
                    "name": "特色阿拉伯比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66021190,
                        "name": "特色阿拉伯比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesealabobisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 43.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/4/c6/9cdba283a0e2fbecaba7fedc159c7jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "tesezhaoshaojibisa",
                    "name": "特色照烧鸡比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66021406,
                        "name": "特色照烧鸡比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tesezhaoshaojibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 43.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/9/65/349e42a02241261481c90aafcf242jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "changxiangyibisa",
                    "name": "肠相依比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66021602,
                        "name": "肠相依比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "changxiangyibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 43.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/4/6a/d8da86bb874173599719df425a053jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "jiduxianghunbisa",
                    "name": "极度香荤比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66021811,
                        "name": "极度香荤比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "jiduxianghunbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 43.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/2/de/3a0f879dc3b3ae53869f0d3d8a22djpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "shizhenhuibisa",
                    "name": "十珍汇比萨",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66022052,
                        "name": "十珍汇比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shizhenhuibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 43.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/f/d2/987d1456b7b9cf12eaee43c73ab78jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiabingxiejiangbisa",
                    "name": "虾兵蟹将比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66022496,
                        "name": "虾兵蟹将比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiabingxiejiangbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/e/3b/c1a89a939684b220c3ca6157d4687jpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "qingxinshujiaobisa",
                    "name": "清馨薯角比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66022710,
                        "name": "清馨薯角比萨",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "qingxinshujiaobisa",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/1/81/37c65ce55122540aa546db412d9c6jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "jinqiangyubisa",
                    "name": "金枪鱼比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66022906,
                        "name": "金枪鱼比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "jinqiangyubisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/2/e8/b5fca0630ccfd685006e282e41967jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "baisazhizunbisa",
                    "name": "百萨至尊比萨",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66023121,
                        "name": "百萨至尊比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "baisazhizunbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 51.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/c/6a/1a7bf072d666701088b4ec15ed4aejpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiangmangkalijibisa",
                    "name": "香芒咖喱鸡比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66023400,
                        "name": "香芒咖喱鸡比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiangmangkalijibisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": "http://fuss10.elemecdn.com/4/1d/5375a09114d437fcea17184c1d58ejpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiandanchaorenbisa",
                    "name": "咸蛋超人比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66023656,
                        "name": "咸蛋超人比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiandanchaorenbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "mingmeitianyuanbisa",
                    "name": "明媚田园比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66020570,
                        "name": "明媚田园比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "mingmeitianyuanbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 39.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "niurouwanbisa",
                    "name": "牛肉丸比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66023767,
                        "name": "牛肉丸比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "niurouwanbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "9寸"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "shuiguobisa",
                    "name": "水果比萨",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66023878,
                        "name": "水果比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shuiguobisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "9寸"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 51.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376182,
                    "image_path": null,
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "liumangbisa-9cun",
                    "name": "榴芒比萨-9寸",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66024073,
                        "name": "榴芒比萨-9寸",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "liumangbisa-9cun",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 86.0,
                        "stock": 9998
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  }
                ],
                "activity": null,
                "is_activity": false,
                "id": 6376182,
                "name": "铁盘系列比萨"
              },
              {
                "description": "",
                "is_selected": false,
                "icon_url": "",
                "foods": [
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/2/79/083c9b2151a9e5453628f3894e52djpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "5个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "tudoujuanxia",
                    "name": "土豆卷虾",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66026446,
                        "name": "土豆卷虾-5个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tudoujuanxia-5ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "5个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 24.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/4/9d/0072840c14a67d07cf8070d992c4djpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "290g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "shuleipinpan",
                    "name": "薯类拼盘",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66027371,
                        "name": "薯类拼盘-290g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shuleipinpan-290g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "290g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 30.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 5.0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/0/8b/205a6af44ed31751174e0581c88d7jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "130g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "tangyangjikuai",
                    "name": "唐扬鸡块",
                    "month_sales": 1,
                    "satisfy_count": 1,
                    "rating_count": 1,
                    "activity": null,
                    "satisfy_rate": 100,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66027987,
                        "name": "唐扬鸡块-130g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tangyangjikuai-130g",
                        "recent_rating": 5.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "130g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 24.0,
                        "stock": 9998
                      }
                    ],
                    "tips": "1评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/f/5c/d114ba65a7a236530aa1aca89fa17jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "300g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "jiroupinpan",
                    "name": "鸡肉拼盘",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66028355,
                        "name": "鸡肉拼盘-300g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "jiroupinpan-300g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "300g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 38.0,
                        "stock": 9998
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/e/d5/53e2d3f940c640b6156d51c5de729jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "4个",
                          "2个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "shaokaojichi",
                    "name": "烧烤鸡翅",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66029244,
                        "name": "烧烤鸡翅-4个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shaokaojichi-4ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "4个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 28.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66029387,
                        "name": "烧烤鸡翅-2个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shaokaojichi-2ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "2个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 15.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 5.0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/c/2a/8e65c897346d74b0938ceb241247djpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "4个",
                          "2个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xianglajichi",
                    "name": "香辣鸡翅",
                    "month_sales": 2,
                    "satisfy_count": 1,
                    "rating_count": 1,
                    "activity": null,
                    "satisfy_rate": 100,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66029599,
                        "name": "香辣鸡翅-4个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xianglajichi-4ge",
                        "recent_rating": 5.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "4个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 28.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 66029601,
                        "name": "香辣鸡翅-2个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xianglajichi-2ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "2个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 15.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "1评价 月售2份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/b/b9/e5030c438354a7e1d63abd08e5a2ajpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "120g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xianglashuge",
                    "name": "香辣薯格",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66029917,
                        "name": "香辣薯格-120g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xianglashuge-120g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "120g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 15.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/9/7e/8eb0a1e155cc788ba08b7c533cc91jpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "yuanweishutiao-150g",
                    "name": "原味薯条-150g",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66030078,
                        "name": "原味薯条-150g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "yuanweishutiao-150g",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 12.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/0/fc/af7dd3c9ef1ca5c0d40a11b334343jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "150g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "qiazhenshutiao",
                    "name": "卡真薯条",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66030316,
                        "name": "卡真薯条-150g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "qiazhenshutiao-150g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "150g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 15.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/6/7d/71091a7dd2aa40bded44969b7c71bjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "6个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiangnongniurouwan",
                    "name": "香浓牛肉丸",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66030538,
                        "name": "香浓牛肉丸-6个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiangnongniurouwan-6ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "6个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 24.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/9/05/064d007af53382f75063855e32560jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "6个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiaolianshubing",
                    "name": "笑脸薯饼",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66030768,
                        "name": "笑脸薯饼-6个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiaolianshubing-6ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "6个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 12.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/c/99/82baab1de2d6b18d35871fe8ab444jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "6个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xiangsuyangcongquan",
                    "name": "香酥洋葱圈",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66031002,
                        "name": "香酥洋葱圈-6个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xiangsuyangcongquan-6ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "6个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 12.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/8/95/d2726dd457c48bec6f91099f5873bjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "4个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xianxiapeigenjuan",
                    "name": "鲜虾培根卷",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66031833,
                        "name": "鲜虾培根卷-4个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xianxiapeigenjuan-4ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "4个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 28.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/f/42/5b5aa48cbe98ac10c346d2aa46486jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "5个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "peigenbeiroujuan",
                    "name": "培根贝肉卷",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66032117,
                        "name": "培根贝肉卷-5个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "peigenbeiroujuan-5ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "5个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 26.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/8/19/7a6a430addbf9c34c9b6dc8f2473ajpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "4根"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "deshikaochang",
                    "name": "德式烤肠",
                    "month_sales": 2,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66032324,
                        "name": "德式烤肠-4根",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "deshikaochang-4gen",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "4根"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 2,
                        "price": 18.0,
                        "stock": 9998
                      }
                    ],
                    "tips": "0评价 月售2份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/7/de/fbd696d334f184df05ac6895a4e26jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "4个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "zhishijuqingbei",
                    "name": "芝士焗青贝",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66032578,
                        "name": "芝士焗青贝-4个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "zhishijuqingbei-4ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "4个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 28.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/5/05/283050b1ffdd05e7f92531ebac2dejpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "4个",
                          "2个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "suanxiangbachi",
                    "name": "蒜香扒翅",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66032912,
                        "name": "蒜香扒翅-4个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "suanxiangbachi-4ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "4个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 25.0,
                        "stock": 9998
                      },
                      {
                        "original_price": null,
                        "food_id": 66032913,
                        "name": "蒜香扒翅-2个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "suanxiangbachi-2ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "2个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 13.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/2/3e/40275885a01b89b2e8c3fe9ca8f88jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "160g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "tezhizhishitiao",
                    "name": "特制芝士条",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66033076,
                        "name": "特制芝士条-160g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tezhizhishitiao-160g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "160g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 22.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": "http://fuss10.elemecdn.com/1/66/831d533deb4e968b751e30ab2b01fjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "2个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "fengweitazhan",
                    "name": "风味塔盏",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66033811,
                        "name": "风味塔盏-2个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "fengweitazhan-2ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "2个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 12.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "120g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "mizhisuanxiangmianbao",
                    "name": "秘制蒜香面包",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66028662,
                        "name": "秘制蒜香面包-120g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "mizhisuanxiangmianbao-120g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "120g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 15.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "6个"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "zhishijuguaniu",
                    "name": "芝士焗蜗牛",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66031399,
                        "name": "芝士焗蜗牛-6个",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "zhishijuguaniu-6ge",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "6个"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 28.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "220g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "nuoweitaiyu",
                    "name": "挪威鲐鱼",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66031666,
                        "name": "挪威鲐鱼-220g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "nuoweitaiyu-220g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "220g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 26.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "220g",
                          "110g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "tankaozhupai",
                    "name": "炭烤猪排",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66033448,
                        "name": "炭烤猪排-220g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tankaozhupai-220g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "220g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 32.0,
                        "stock": 10000
                      },
                      {
                        "original_price": null,
                        "food_id": 66033449,
                        "name": "炭烤猪排-110g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "tankaozhupai-110g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "110g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 18.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376212,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "大份",
                          "小份"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "shijinzaban",
                    "name": "什锦杂拌",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66034199,
                        "name": "什锦杂拌-大份",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shijinzaban-dafen",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "大份"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 28.0,
                        "stock": 9999
                      },
                      {
                        "original_price": null,
                        "food_id": 66034201,
                        "name": "什锦杂拌-小份",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shijinzaban-xiaofen",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "小份"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 22.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  }
                ],
                "activity": null,
                "is_activity": false,
                "id": 6376212,
                "name": "精品小吃"
              },
              {
                "description": "",
                "is_selected": false,
                "icon_url": "",
                "foods": [
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376214,
                    "image_path": "http://fuss10.elemecdn.com/4/5e/a7e8b18ac7f87294438ecac56555cjpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "shucaishala",
                    "name": "蔬菜沙拉",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66034452,
                        "name": "蔬菜沙拉",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shucaishala",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 15.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376214,
                    "image_path": "http://fuss10.elemecdn.com/0/ef/a1a119cfd2249cd9d0536291c48ddjpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "shuiguoshala",
                    "name": "水果沙拉",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66034715,
                        "name": "水果沙拉",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shuiguoshala",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 22.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376214,
                    "image_path": "http://fuss10.elemecdn.com/6/d7/4bc92b11616fd5c59d495c5aaf5c3jpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "jinqiangyushala",
                    "name": "金枪鱼沙拉",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66034863,
                        "name": "金枪鱼沙拉",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "jinqiangyushala",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 24.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376214,
                    "image_path": "http://fuss10.elemecdn.com/b/76/3af79f86e4c27b69da715d8292715jpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "kaisashala",
                    "name": "凯撒沙拉",
                    "month_sales": 1,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66035182,
                        "name": "凯撒沙拉",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "kaisashala",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 1,
                        "price": 15.0,
                        "stock": 9999
                      }
                    ],
                    "tips": "0评价 月售1份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376214,
                    "image_path": "http://fuss10.elemecdn.com/5/a9/940fff73ed74d29818c9570cad878jpeg.jpeg",
                    "specifications": [],
                    "restaurant_id": 725427,
                    "pinyin_name": "eshishala",
                    "name": "俄式沙拉",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66035417,
                        "name": "俄式沙拉",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "eshishala",
                        "recent_rating": 0.0,
                        "specs": [],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 16.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  }
                ],
                "activity": null,
                "is_activity": false,
                "id": 6376214,
                "name": "沙拉"
              },
              {
                "description": "",
                "is_selected": false,
                "icon_url": "",
                "foods": [
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376218,
                    "image_path": "http://fuss10.elemecdn.com/a/4e/85ada78b76016356812d524451e0ajpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "260g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "feiliniupai",
                    "name": "菲力牛排",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66035708,
                        "name": "菲力牛排-260g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "feiliniupai-260g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "260g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 56.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376218,
                    "image_path": "http://fuss10.elemecdn.com/6/94/9bac825b9621016fab44e563aed15jpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "240g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xilengniupai",
                    "name": "西冷牛排",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66035989,
                        "name": "西冷牛排-240g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xilengniupai-240g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "240g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 52.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376218,
                    "image_path": "http://fuss10.elemecdn.com/e/e7/cce896e4ac2414a4408da758e5c7cjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "230g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "shalangniupai",
                    "name": "沙朗牛排",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66036195,
                        "name": "沙朗牛排-230g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shalangniupai-230g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "230g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 46.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376218,
                    "image_path": "http://fuss10.elemecdn.com/e/e7/cce896e4ac2414a4408da758e5c7cjpeg.jpeg",
                    "specifications": [
                      {
                        "values": [
                          "230g"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "shalangniupai",
                    "name": "沙朗牛排",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66036456,
                        "name": "沙朗牛排-230g",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "shalangniupai-230g",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "230g"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 46.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  }
                ],
                "activity": null,
                "is_activity": false,
                "id": 6376218,
                "name": "精品牛排"
              },
              {
                "description": "",
                "is_selected": false,
                "icon_url": "",
                "foods": [
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376226,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "280ml"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xingbakekafei",
                    "name": "星巴克咖啡",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66036726,
                        "name": "星巴克咖啡-280ml",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xingbakekafei-280ml",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "280ml"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 28.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376226,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "330ml"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "kele",
                    "name": "可乐",
                    "month_sales": 7,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66037432,
                        "name": "可乐-330ml",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "kele-330ml",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "330ml"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 7,
                        "price": 5.0,
                        "stock": 9991
                      }
                    ],
                    "tips": "0评价 月售7份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376226,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "330ml"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xuebi",
                    "name": "雪碧",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66037588,
                        "name": "雪碧-330ml",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xuebi-330ml",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "330ml"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 5.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376226,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "330ml"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "fenda",
                    "name": "芬达",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66037742,
                        "name": "芬达-330ml",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "fenda-330ml",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "330ml"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 5.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376226,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "1.25L"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "kele",
                    "name": "可乐",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66039478,
                        "name": "可乐-1.25L",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "kele-1.25L",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "1.25L"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 10.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376226,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "1.25L"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "xuebi",
                    "name": "雪碧",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66040061,
                        "name": "雪碧-1.25L",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "xuebi-1.25L",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "1.25L"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 10.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  },
                  {
                    "rating": 0,
                    "limitation": {},
                    "category_id": 6376226,
                    "image_path": null,
                    "specifications": [
                      {
                        "values": [
                          "550ml"
                        ],
                        "name": "规格"
                      }
                    ],
                    "restaurant_id": 725427,
                    "pinyin_name": "kunlunshan",
                    "name": "昆仑山",
                    "month_sales": 0,
                    "satisfy_count": 0,
                    "rating_count": 0,
                    "activity": null,
                    "satisfy_rate": 0,
                    "specfoods": [
                      {
                        "original_price": null,
                        "food_id": 66040450,
                        "name": "昆仑山-550ml",
                        "restaurant_id": 725427,
                        "packing_fee": 0.0,
                        "pinyin_name": "kunlunshan-550ml",
                        "recent_rating": 0.0,
                        "specs": [
                          {
                            "name": "规格",
                            "value": "550ml"
                          }
                        ],
                        "sold_out": false,
                        "recent_popularity": 0,
                        "price": 8.0,
                        "stock": 10000
                      }
                    ],
                    "tips": "0评价 月售0份",
                    "attributes": [],
                    "description": ""
                  }
                ],
                "activity": null,
                "is_activity": false,
                "id": 6376226,
                "name": "饮品"
              }
            ]

### baidu

