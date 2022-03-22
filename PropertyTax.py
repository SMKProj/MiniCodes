#Exercie 3 Property Tax
val = input("Enter actual value of your owned piece of property: ")
property_val = float(val)
property_assessment_val = float(0.6 * property_val)
hunderedth_of_assesment_val = (property_assessment_val / 100)
percentage = hunderedth_of_assesment_val / 100
property_tax = float( percentage * 72)

print("-------------------------------------------------------------")
print("Property Value", "\t" , "Assessment Value", "\t" , "Tax Value")
print("$",property_val, "\t", "$", property_assessment_val, "\t\t", "¢ "'{:.2f}'.format(property_tax))


