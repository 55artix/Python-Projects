### Early Feedback for Homework 10 (THIS IS NOT YOUR GRADE, the assignment isn't due yet)

These tests are run on Monday and Tuesday nights around 11:55 PM, so if you didn't submit before then you can ignore this document

Passing these tests is not a guarantee of a perfect homework score: the tests do not check everything that the TAs will.

Any questions/errors with the Automated Feedback should be reported to Nathan Taylor: taylo740@umn.edu

Run on November 12, 03:41:43 AM.

+ Pass: Change into directory "hw10".

+ Pass: Check that file "hw10.py" exists.

+ Pass: Secret Test

+ Pass: Check that a Python file "hw10.py" has no syntax errors.

    Python file "hw10.py" has no syntax errors.



+ Pass: Writing normandy.csv into local directory  
File Contents:
```
Location,Normandy,,,
Upkeep,46220.76,,,
Name,Position,Salary,Years with Company,Value
Shepard,Operational Analytics Specialist,12268.38,2.0,68469.18
Kaiden,Creative Logistics Technician,42769.73,7.8,33298.00
Ashley,Efficiency Services Technician,37082.97,4.4,66892.43
Wrex,Efficiency Analytics Engineer,34273.76,5.0,96375.57
Garrus,Data Services Consultant,45248.14,7.5,20014.88
Tali,Data Services Coordinator,61158.97,9.8,61379.63
Liara,Enterprise Evolution Technician,35916.35,0.8,43490.50

```




+ Pass: Writing rogueport.csv into local directory  
File Contents:
```
Location,Rogueport,,,
Upkeep,25644.07,,,
Name,Position,Salary,Years with Company,Value
Mario,Efficiency Communications Technician,54739.83,0.0,86436.96
Goombella,Creative Logistics Specialist,83061.62,0.8,4984.78
Koops,Efficiency Services Strategist,49912.50,15.6,84064.77
Flurrie,Operational Services Consultant,17189.48,9.6,83015.18
Yoshi,Enterprise Logistics Engineer,62324.82,15.4,58877.99
Vivian,Creative Innovation Strategist,39072.89,11.4,44350.42
Bobbery,Creative Communications Specialist,12996.65,12.5,6379.13
Mowz,Operational Analytics Strategist,68166.70,6.9,30004.22

```




+ Pass: Writing guardia.csv into local directory  
File Contents:
```
Location,Guardia,,,
Upkeep,63105.73,,,
Name,Position,Salary,Years with Company,Value
Chrono,Data Services Engineer,45395.44,2.4,8690.64
Marle,Operational Analytics Consultant,21069.78,15.3,52140.23
Lucca,Efficiency Evolution Consultant,18207.42,18.1,67924.10
Frog,Efficiency Communications Specialist,20479.80,8.7,54057.60
Robo,Efficiency Analytics Coordinator,44149.63,11.4,59078.81
Ayla,Efficiency Logistics Coordinator,36568.99,1.0,51512.07
Magus,Enterprise Analytics Strategist,23906.50,11.4,67649.59

```




+ Pass: 
Check that the result of evaluating
   ```
   Complex(4,3).get_real()
   ```
   matches the pattern `4`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Complex(-4,12).get_imag()
   ```
   matches the pattern `12`.

   




+ Pass: 
Check that the result of evaluating
   ```
   a = Complex(2,7); a.set_real(5); a.real
   ```
   matches the pattern `5`.

   




+ Pass: 
Check that the result of evaluating
   ```
   a = Complex(3,0); a.set_imag(-8); a.imag
   ```
   matches the pattern `-8`.

   




+ Pass: 
Check that the result of evaluating
   ```
   str(Complex(6,77))
   ```
   matches the pattern `'6 + 77i'`.

   




+ Pass: 
Check that the result of evaluating
   ```
   (Complex(-1,6) + Complex(5,-9)).real
   ```
   matches the pattern `4`.

   




+ Pass: 
Check that the result of evaluating
   ```
   (Complex(-1,6) + Complex(5,-9)).imag
   ```
   matches the pattern `-3`.

   




+ Pass: 
Check that the result of evaluating
   ```
   (Complex(-1,6) * Complex(5,-9)).real
   ```
   matches the pattern `49`.

   




+ Pass: 
Check that the result of evaluating
   ```
   (Complex(-1,6) * Complex(5,-9)).imag
   ```
   matches the pattern `39`.

   




+ Pass: 
Check that the result of evaluating
   ```
   (Complex(-1,6) == Complex(-1,6))
   ```
   matches the pattern `True`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Employee('n,p,1.00,2.00,4.00\n').name
   ```
   matches the pattern `'n'`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Employee('n,p,1.00,2.00,4.00\n').position
   ```
   matches the pattern `'p'`.

   




+ Pass: 
Check that the result of evaluating
   ```
   0.99 < Employee('n,p,1.00,2.00,4.00\n').salary < 1.01
   ```
   matches the pattern `True`.

   




+ Pass: 
Check that the result of evaluating
   ```
   1.99 < Employee('n,p,1.00,2.00,4.00\n').seniority < 2.01
   ```
   matches the pattern `True`.

   




+ Pass: 
Check that the result of evaluating
   ```
   3.99 < Employee('n,p,1.00,2.00,4.00\n').value < 4.01
   ```
   matches the pattern `True`.

   




+ Pass: 
Check that the result of evaluating
   ```
   str(Employee('n,p,1.00,2.00,4.00\n'))
   ```
   matches the pattern `'n, p'`.

   




+ Pass: 
Check that the result of evaluating
   ```
   2.99 < Employee('n,p,1.00,2.00,4.00\n').net_value() < 3.01
   ```
   matches the pattern `True`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Employee('n,p,1.00,2.00,4.00\n') < Employee('n,p,4.00,2.00,1.00\n')
   ```
   matches the pattern `False`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Branch('normandy.csv').location
   ```
   matches the pattern `'Normandy'`.

   




+ Pass: 
Check that the result of evaluating
   ```
   46220.75 < Branch('normandy.csv').upkeep < 46220.77
   ```
   matches the pattern `True`.

   




+ Pass: 
Check that the result of evaluating
   ```
   len(Branch('normandy.csv').team)
   ```
   matches the pattern `7`.

   




+ Fail: 
Check that the result of evaluating
   ```
   {emp.name for emp in Branch('normandy.csv').team}
   ```
   matches the pattern `{'Shepard','Kaiden','Ashley','Garrus','Tali','Wrex','Liara'}`.

   


   Test failed. The following errors were reported:

```
 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <setcomp>
AttributeError: 'str' object has no attribute 'name'
```


+ Pass: 
Check that the result of evaluating
   ```
   str(Employee('Wrex,Efficiency Analytics Engineer,34273.76,5.0,96375.57\n')) in str(Branch('normandy.csv'))
   ```
   matches the pattern `True`.

   




+ Pass: 
Check that the result of evaluating
   ```
   74981.12 < Branch('normandy.csv').profit() < 74981.14
   ```
   matches the pattern `True`.

   




+ Fail: 
Check that the result of evaluating
   ```
   Branch('rogueport.csv') < Branch('normandy.csv')
   ```
   matches the pattern `True`.

   


   Test failed. The following errors were reported:

```
 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw10.py", line 231, in __lt__
    if self.profit()<other.profit:
TypeError: '<' not supported between instances of 'float' and 'method'
```


+ Fail: 
Check that the result of evaluating
   ```
   brn = Branch('normandy.csv'); brn.cut(4); {emp.name for emp in brn.team}
   ```
   matches the pattern `{'Shepard','Ashley','Wrex'}`.

   


   Test failed. The following errors were reported:

```
 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <setcomp>
AttributeError: 'str' object has no attribute 'name'
```


+ Pass: 
Check that the result of evaluating
   ```
   Company('Zzzzz', [Branch('normandy.csv'),Branch('rogueport.csv'),Branch('guardia.csv')]).name
   ```
   matches the pattern `'Zzzzz'`.

   




+ Pass: 
Check that the result of evaluating
   ```
   str(Branch('rogueport.csv')) in str(Company('Zzzzz', [Branch('normandy.csv'),Branch('rogueport.csv'),Branch('guardia.csv')]))
   ```
   matches the pattern `True`.

   




+ Fail: 
Check that the result of evaluating
   ```
   cmp = Company('Zzzzz', [Branch('guardia.csv')]); cmp.synergize(); {emp.name for bnch in cmp.branches for emp in bnch.team}
   ```
   matches the pattern `{'Marle','Lucca','Frog','Magus'}`.

   


   Test failed. The following errors were reported:

```
 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <setcomp>
AttributeError: 'str' object has no attribute 'name'
```


+ Fail: 
Check that the result of evaluating
   ```
   cmp = Company('Zzzzz', [Branch('normandy.csv'),Branch('rogueport.csv'),Branch('guardia.csv')]); cmp.synergize(); {emp.name for bnch in cmp.branches for emp in bnch.team}
   ```
   matches the pattern `{'Shepard','Kaiden','Ashley','Garrus','Tali','Wrex','Liara','Mario','Koops','Flurrie','Vivian','Chrono','Marle','Lucca','Frog','Robo','Ayla','Magus'}`.

   


   Test failed. The following errors were reported:

```
 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <setcomp>
AttributeError: 'str' object has no attribute 'name'
```


