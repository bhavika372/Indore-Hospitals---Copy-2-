from asyncio.windows_events import NULL
from email.policy import default
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///hospitalinfo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #set to false to disable tracking and use less memory
db = SQLAlchemy(app)


class hospital(db.Model):

    # info section
    sno = db.Column(db.Integer, primary_key=True)
    hospital_type = db.Column(db.String(20), nullable=False)
    hospital_name = db.Column(db.String(20), nullable=False)
    hospital_desc = db.Column(db.String(200), nullable=False)
    hospital_contact = db.Column(db.String(30), nullable=False)
    primary_email_id = db.Column(db.String(30), default="NULL")
    secondary_email_id = db.Column(db.String(30), default="NULL")
    hospital_address = db.Column(db.String(100), nullable=False)
    hospital_pincode = db.Column(db.Integer, nullable=False)
    hospital_city = db.Column(db.String(40), nullable= False)
    hospital_state = db.Column(db.String(40), nullable= False)
    hospital_registration_number = db.Column(db.Integer, nullable=False)
    # nodal information
    nodal_person_name_and_designation = db.Column(db.String(100), nullable=False)
    nodal_person_telephone_number = db.Column(db.Integer, nullable=False)
    nodal_person_email_id = db.Column(db.String(30), default="NULL")
    # beds info
    total_general_beds = db.Column(db.Integer, nullable=False)
    available_general_beds = db.Column(db.Integer, nullable=False)
    total_oxygen_beds = db.Column(db.Integer, nullable=False)
    available_oxygen_beds = db.Column(db.Integer, nullable=False)
    total_icu_beds = db.Column(db.Integer, nullable=False)
    available_icu_beds = db.Column(db.Integer, nullable=False)
    total_icu_beds_with_ventilator = db.Column(db.Integer, nullable=False)
    available_icu_beds_with_ventilator = db.Column(db.Integer, nullable=False)
    total_ews_beds = db.Column(db.Integer, nullable=False)
    available_ews_beds = db.Column(db.Integer, nullable=False)
    total_private_wards = db.Column(db.Integer, nullable=False)
    available_private_wards = db.Column(db.Integer, nullable=False)
   # login essentials
    login_passcode = db.Column(db.String(15), nullable=False)
    
    #Facilities
    ICU = db.Column(db.String(20), nullable=False)
    IPD = db.Column(db.String(20), nullable=False)
    OPD = db.Column(db.String(20), nullable=False)
    Laboratory = db.Column(db.String(20), nullable=False)
    Pharmacy = db.Column(db.String(20), nullable=False)
    Labour_Room = db.Column(db.String(20), nullable=False)
    Blood_Bank = db.Column(db.String(20), nullable=False)
    Blood_Storage = db.Column(db.String(20), nullable=False)
    Organ_Bank = db.Column(db.String(20), nullable=False)
    Ambulance = db.Column(db.String(20), nullable=False)
    Dialysis_Unit = db.Column(db.String(20), nullable=False)
    Operation_Theatre = db.Column(db.String(20), nullable=False)
    Physiotherapy = db.Column(db.String(20), nullable=False)
    MRI = db.Column(db.String(20), nullable=False)
    CT_Scan = db.Column(db.String(20), nullable=False)
    Occupational_Therapy = db.Column(db.String(20), nullable=False)

    # miscellanous facilities
    total_no_of_doctors = db.Column(db.Integer, nullable=False)
    number_of_ambulances = db.Column(db.Integer, nullable=False)
    blood_bank_number = db.Column(db.Integer, nullable=False)
    
    hospital_provider_type = db.Column(db.String(50), nullable=False)


    def __repr__(self) -> str:
        return f"{self.sno}-{self.hospital_name}"




@app.route("/", methods=['GET', 'POST'])
def index():
    args = request.args
    arg = args.get("type")
    if arg :
        obj=hospital.query.filter_by(hospital_type=arg).all()
    else :
        obj = hospital.query.all()
    
    return render_template('index.html', obj=obj)



@app.route("/moreinfo/<int:sno>",methods=['GET','POST'])
def moreinfo(sno):
    obj=hospital.query.filter_by(sno=sno).first()
    return render_template('moreinfo.html',obj=obj)
    
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        primary_email_id = request.form['primary_email_id']
        login_passcode = request.form['login_passcode']
        if primary_email_id=='bhavik.mundra1603@gmail.com' and login_passcode=='Bhavik1603*':
            obj=hospital.query.all()
            return redirect('/admin')
        if primary_email_id=='bhavika.darpe@gmail.com' and login_passcode=='Bhavika37':
            obj=hospital.query.all()
            return redirect('/admin')
        obj = hospital.query.filter_by(primary_email_id=primary_email_id).first()
        if obj.login_passcode == login_passcode:
            return redirect(f"/update/{obj.sno}")
    return render_template('login.html')


@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        nodal_person_name_and_designation = request.form['nodal_person_name_and_designation']
        nodal_person_telephone_number = request.form['nodal_person_telephone_number']
        nodal_person_email_id = request.form['nodal_person_email_id']
        # beds info
        total_general_beds = request.form['total_general_beds']
        available_general_beds = request.form['available_general_beds']
        total_oxygen_beds = request.form['total_oxygen_beds']
        available_oxygen_beds = request.form['available_oxygen_beds']
        total_icu_beds = request.form['total_icu_beds']
        available_icu_beds = request.form['available_icu_beds']
        total_icu_beds_with_ventilator = request.form['total_icu_beds_with_ventilator']
        available_icu_beds_with_ventilator = request.form['available_icu_beds_with_ventilator']
        total_ews_beds = request.form['total_ews_beds']
        available_ews_beds = request.form['available_ews_beds']
        total_private_wards = request.form['total_private_wards']
        available_private_wards = request.form['available_private_wards']
        
        # miscellanous facilities
        total_no_of_doctors = request.form['total_no_of_doctors']
       
        number_of_ambulances = request.form['number_of_ambulances']
        blood_bank_number = request.form['blood_bank_number']
        
        #facilities
        ICU = request.form['ICU']
        IPD = request.form['IPD']
        OPD = request.form['OPD']
        Laboratory = request.form['Laboratory']
        Pharmacy = request.form['Pharmacy']
        Labour_Room = request.form['Labour_Room']
        Blood_Bank = request.form['Blood_Bank']
        Blood_Storage = request.form['Blood_Storage']
        Organ_Bank = request.form['Organ_Bank']
        Ambulance = request.form['Ambulance']
        Dialysis_Unit = request.form['Dialysis_Unit']
        Operation_Theatre = request.form['Operation_Theatre']
        Physiotherapy = request.form['Physiotherapy']
        MRI = request.form['MRI']
        CT_Scan = request.form['CT_Scan']
        Dialysis_Unit = request.form['Dialysis_Unit']
        Occupational_Therapy = request.form['Occupational_Therapy']

        obj = hospital.query.filter_by(sno=sno).first()
        obj.nodal_person_name_and_designation = nodal_person_name_and_designation
        obj.nodal_person_telephone_number = nodal_person_telephone_number
        obj.nodal_person_email_id = nodal_person_email_id
        # beds info
        obj.total_general_beds = total_general_beds
        obj.available_general_beds = available_general_beds
        obj.total_oxygen_beds = total_oxygen_beds
        obj.available_oxygen_beds = available_oxygen_beds
        obj.total_icu_beds = total_icu_beds
        obj.available_icu_beds = available_icu_beds
        obj.total_icu_beds_with_ventilator = total_icu_beds_with_ventilator
        obj.available_icu_beds_with_ventilator = available_icu_beds_with_ventilator
        obj.total_ews_beds = total_ews_beds
        obj.available_ews_beds = available_ews_beds
        obj.total_private_wards = total_private_wards
        obj.available_private_wards = available_private_wards
        obj.total_no_of_doctors = total_no_of_doctors
        obj.number_of_ambulances = number_of_ambulances
        obj.blood_bank_number = blood_bank_number
        #facilities
        obj.ICU = ICU
        obj.IPD = IPD
        obj.OPD = OPD
        obj.Laboratory = Laboratory
        obj.Pharmacy = Pharmacy
        obj.Labour_Room = Labour_Room
        obj.Blood_Bank = Blood_Bank
        obj.Blood_Storage = Blood_Storage
        obj.Organ_Bank = Organ_Bank
        obj.Ambulance = Ambulance
        obj.Dialysis_Unit = Dialysis_Unit
        obj.Operation_Theatre = Operation_Theatre
        obj.Physiotherapy = Physiotherapy
        obj.MRI = MRI
        obj.CT_Scan = CT_Scan
        obj.Occupational_Therapy = Occupational_Therapy

        db.session.add(obj)
        db.session.commit()
    obj = hospital.query.filter_by(sno=sno).first()
    return render_template('update.html', obj=obj)


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        hospital_type = request.form['hospital_type']
        hospital_name = request.form['hospital_name']
        hospital_desc = request.form['hospital_desc']
        hospital_contact = request.form['hospital_contact']
        primary_email_id = request.form['primary_email_id']
        secondary_email_id = request.form['secondary_email_id']
        hospital_address = request.form['hospital_address']
        hospital_pincode = request.form['hospital_pincode']
        hospital_city = request.form['hospital_city']
        hospital_state = request.form['hospital_state']
        hospital_registration_number = request.form['hospital_registration_number']
        # nodal information
        nodal_person_name_and_designation = request.form['nodal_person_name_and_designation']
        nodal_person_telephone_number = request.form['nodal_person_telephone_number']
        nodal_person_email_id = request.form['nodal_person_email_id']
        # beds info
        total_general_beds = request.form['total_general_beds']
        available_general_beds = request.form['available_general_beds']
        total_oxygen_beds = request.form['total_oxygen_beds']
        available_oxygen_beds = request.form['available_oxygen_beds']
        total_icu_beds = request.form['total_icu_beds']
        available_icu_beds = request.form['available_icu_beds']
        total_icu_beds_with_ventilator = request.form['total_icu_beds_with_ventilator']
        available_icu_beds_with_ventilator = request.form['available_icu_beds_with_ventilator']
        total_ews_beds = request.form['total_ews_beds']
        available_ews_beds = request.form['available_ews_beds']
        total_private_wards = request.form['total_private_wards']
        available_private_wards = request.form['available_private_wards']
        # login essentials
        login_passcode = request.form['login_passcode']

        #facilities
        ICU = request.form['ICU']
        IPD = request.form['IPD']
        OPD = request.form['OPD']
        Laboratory = request.form['Laboratory']
        Pharmacy = request.form['Pharmacy']
        Labour_Room = request.form['Labour_Room']
        Blood_Bank = request.form['Blood_Bank']
        Blood_Storage = request.form['Blood_Storage']
        Organ_Bank = request.form['Organ_Bank']
        Ambulance = request.form['Ambulance']
        Dialysis_Unit = request.form['Dialysis_Unit']
        Operation_Theatre = request.form['Operation_Theatre']
        Physiotherapy = request.form['Physiotherapy']
        MRI = request.form['MRI']
        CT_Scan = request.form['CT_Scan']
        Occupational_Therapy = request.form['Occupational_Therapy']


        # miscellanous facilities
        total_no_of_doctors = request.form['total_no_of_doctors']
        # contact number of ambulance driver
        number_of_ambulances = request.form['number_of_ambulances']
        blood_bank_number = request.form['blood_bank_number']

        hospital_provider_type =request.form['hospital_provider_type']
        obj = hospital(hospital_provider_type=hospital_provider_type,total_no_of_doctors=total_no_of_doctors, number_of_ambulances=number_of_ambulances, blood_bank_number=blood_bank_number, hospital_type=hospital_type, hospital_name=hospital_name, hospital_desc=hospital_desc, hospital_contact=hospital_contact, primary_email_id=primary_email_id, secondary_email_id=secondary_email_id, hospital_address=hospital_address,hospital_city=hospital_city,hospital_state=hospital_state, hospital_pincode=hospital_pincode, hospital_registration_number=hospital_registration_number, nodal_person_email_id=nodal_person_email_id, nodal_person_name_and_designation=nodal_person_name_and_designation,
                       nodal_person_telephone_number=nodal_person_telephone_number, total_ews_beds=total_ews_beds, available_ews_beds=available_ews_beds, total_general_beds=total_general_beds, available_general_beds=available_general_beds, total_icu_beds=total_icu_beds, available_icu_beds=available_icu_beds, total_icu_beds_with_ventilator=total_icu_beds_with_ventilator, available_icu_beds_with_ventilator=available_icu_beds_with_ventilator, total_oxygen_beds=total_oxygen_beds, available_oxygen_beds=available_oxygen_beds, total_private_wards=total_private_wards, available_private_wards=available_private_wards, login_passcode=login_passcode,ICU=ICU, IPD=IPD, OPD=OPD, Laboratory=Laboratory, Pharmacy=Pharmacy, Labour_Room=Labour_Room, Blood_Bank=Blood_Bank, Blood_Storage=Blood_Storage, Organ_Bank=Organ_Bank, Ambulance=Ambulance, Dialysis_Unit=Dialysis_Unit, Operation_Theatre=Operation_Theatre, Physiotherapy=Physiotherapy, MRI=MRI, CT_Scan=CT_Scan, Occupational_Therapy=Occupational_Therapy)
        db.session.add(obj)
        db.session.commit()
        return redirect('/login')

    return render_template('registration.html')


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    obj = hospital.query.all()
    return render_template("admin.html", obj=obj)

@app.route("/deleteHospitalAccountByAdmin/<int:sno>")
def deleteHospitalByAdmin(sno):
    obj_ = hospital.query.filter_by(sno=sno).first()
    db.session.delete(obj_)
    db.session.commit()
    return redirect("/admin")

if __name__ == "__main__":
    app.run(debug=True, port=5050)
