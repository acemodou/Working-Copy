# Simple hello ruby to add two numbers 
# print "Enter a value: "

# first_num = gets.to_i

# print "Another value: "

# second_num = gets.to_i

# puts first_num.to_s + "+" + second_num.to_s + " = " + (first_num + second_num).to_s

#This shows that every thing is an object in ruby 
# puts 1.class
# puts 1.34.class 


# A_CONSTANT = 3.14

# A_CONSTANT = 6

# puts A_CONSTANT

# Writing and reading a file 
# write_handler = File.new("mytext.out", "w")
# write_handler.puts("Random text").to_s 

# write_handler.close

# data_from_file = File.read("mytext.out")

# puts "Data from file: " + data_from_file 

# age = 50

# Ternanry operators 

# puts (age >= 50) ? "old" : "Young"

# if (age >= 5) && (age <= 6)
#     puts "You are a toddler"
# elsif (age >= 7) && (age <= 13)
#     puts "You 're in Middle School"
# else
#     puts "Stay at home"
# end 

# unless age > 4
#     puts "No School"
# else
#     puts "Go to school"
# end 


# puts " You're young" if age < 30 


# Switch cases 
# print "Enter greetings : "
# greetings = gets.chomp 

# case greetings
# when "french"
#     puts "bonjour"
#     exit 
# when "spanish"
#     puts "hola"
#     exit 
# else "english"
#     puts "hello"
# end 


# x = 1
# loop do
#     x += 1

#     next unless (x % 2) == 0
#     puts x

#     break if x >= 10
# end

# y = 1
#  while y <= 10
#     y += 1
#     next unless (y % 2) == 0
#     puts y 
#  end 

# a = 1 

# until  a >= 10
#     a += 1
#     next unless (a % 2) == 0
#     puts a 
     
# end

# numbers = [1, 3, 7]

# for num in numbers 
#     print "#{num},"
# end 

# groceries = ["bananas", "sweet potatoes", "pasta", "tomatoes"]


# groceries.each do |food|
#     puts "Get some #{food}"
# end 

# (0..5).each do |i|
#     puts "# #{i}"
# end 

# def add_nums(num_1, num_2)
#     return num_1.to_i + num_2.to_i
# end 

# puts add_nums(3,4)

# print "Enter a Number: "
# first_num = gets.to_i 
# print "Enter another: "
# second_num = gets.to_i 

# begin
#     answer = first_num / second_num
# rescue
#     puts "You can't divide by zero"
#     exit 
# end

# puts "#{first_num} / #{second_num} = #{answer}"

# age = 12 

# def check_age(age)
#     raise ArgumentError, "Enter positive number " unless age > 0
#     exit 
# end 

# begin
#     check_age(-1)
# rescue ArgumentError
#     puts "That is an impossible age"
# end 


# Strings 
# first_name = "Imran"
# last_name = "Jaw"


# full_name = "#{first_name} #{last_name}"

# puts full_name.include?("Im")
# puts full_name.size
# puts "vowels: " + full_name.count("aeiou").to_s
# puts "Consonant: " + full_name.count("^aeiou").to_s 

# puts full_name.start_with?("im")
# puts "index of " + full_name.index("Im").to_s

# puts full_name.chop
# puts full_name.chomp("aw")

# puts full_name.delete("a")
# name_array = full_name.split(//)
# puts name_array 
# name_array = full_name.split(/ /)
# puts name_array 

# class Animal
#     def initialize
#         puts "Creating a New Animal"
#     end 

#     def set_name(new_name)
#         if new_name.is_a?(Numeric)
#             puts "Name can't be a number"
#         end 
#         @name = new_name
#     end 

#     def get_name
#         @name
#     end 
# end 

# cat = Animal.new 
# cat.set_name("Peekabo")
# puts cat.get_name


# class Dog
#     attr_accessor :name, :height, :weight

#     def bark 
#         return "woof"
#     end 
# end 

# dog = Dog.new 
# dog.name = "Topsy"
# puts dog.name 

# class GermanShepard < Dog 
#     def bark
#         return "howl"
#     end 
# end 

# max_dog = GermanShepard.new 
# max_dog.name = "wilson"
# printf "%s goes %s \n", max_dog.name, max_dog.bark 

# require_relative "human"
# require_relative "smart"

# class Scientist
#     include Human
#     prepend Smart 

#     def act_smart
#         return "E = mc^2"
#     end 
# end 

# einstein = Scientist.new 
# einstein.name = "Albert"
# puts einstein.name 
# einstein.run 

# puts einstein.name + " says" + einstein.act_smart

number_hash = { "PI" => 3.14, "Gold" => 3.14, "e" => 3.14 }

puts number_hash["PI"]

# another way 
superheroes = Hash["Clark Kent", "Superman", "Bruce Wayne", "Batman"]
puts superheroes["Bruce Wayne"]

superheroes["Barry Allen"] = "Flash"