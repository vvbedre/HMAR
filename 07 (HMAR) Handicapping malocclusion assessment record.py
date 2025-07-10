import tkinter as tk
from tkinter import ttk, messagebox

class HMARApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Handicapping Malocclusion Assessment Record (HMAR)")
        self.root.geometry("900x700")
        
        # Create notebook for different sections
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)
        
        # Create frames for each section
        self.intra_arch_frame = ttk.Frame(self.notebook)
        self.inter_arch_frame = ttk.Frame(self.notebook)
        self.deformities_frame = ttk.Frame(self.notebook)
        self.results_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.intra_arch_frame, text="Intra-arch Deviations")
        self.notebook.add(self.inter_arch_frame, text="Inter-arch Deviations")
        self.notebook.add(self.deformities_frame, text="Dentofacial Deformities")
        self.notebook.add(self.results_frame, text="Results & Interpretation")
        
        # Initialize variables and create UI elements
        self.create_intra_arch_section()
        self.create_inter_arch_section()
        self.create_deformities_section()
        self.create_results_section()
        
        # Add calculate and reset buttons
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(self.button_frame, text="Calculate Score", command=self.calculate_score).pack(side='left', padx=5)
        ttk.Button(self.button_frame, text="Reset Form", command=self.reset_form).pack(side='left', padx=5)
        ttk.Button(self.button_frame, text="Show Ideal Values", command=self.show_ideal_values).pack(side='right', padx=5)
        
        # Initialize scores
        self.intra_arch_score = 0
        self.inter_arch_score = 0
        self.deformities_score = 0
        self.total_score = 0
        
    def create_intra_arch_section(self):
        # Intra-arch deviations
        ttk.Label(self.intra_arch_frame, text="Intra-arch Deviations", font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=3, pady=5)
        
        # Missing teeth
        self.missing_teeth_var = tk.IntVar(value=0)
        ttk.Label(self.intra_arch_frame, text="Missing teeth (per tooth):").grid(row=1, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.intra_arch_frame, from_=0, to=32, textvariable=self.missing_teeth_var, width=5).grid(row=1, column=1)
        ttk.Label(self.intra_arch_frame, text="Weight: 3").grid(row=1, column=2, padx=5)
        
        # Crowding
        self.crowding_var = tk.IntVar(value=0)
        ttk.Label(self.intra_arch_frame, text="Crowding (mm per arch):").grid(row=2, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.intra_arch_frame, from_=0, to=20, textvariable=self.crowding_var, width=5).grid(row=2, column=1)
        ttk.Label(self.intra_arch_frame, text="Weight: 2").grid(row=2, column=2, padx=5)
        
        # Rotation
        self.rotation_var = tk.IntVar(value=0)
        ttk.Label(self.intra_arch_frame, text="Rotation (degrees per tooth):").grid(row=3, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.intra_arch_frame, from_=0, to=90, textvariable=self.rotation_var, width=5).grid(row=3, column=1)
        ttk.Label(self.intra_arch_frame, text="Weight: 1").grid(row=3, column=2, padx=5)
        
        # Spacing
        self.spacing_var = tk.IntVar(value=0)
        ttk.Label(self.intra_arch_frame, text="Spacing (mm per arch):").grid(row=4, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.intra_arch_frame, from_=0, to=20, textvariable=self.spacing_var, width=5).grid(row=4, column=1)
        ttk.Label(self.intra_arch_frame, text="Weight: 1").grid(row=4, column=2, padx=5)
        
    def create_inter_arch_section(self):
        # Inter-arch deviations
        ttk.Label(self.inter_arch_frame, text="Inter-arch Deviations", font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=3, pady=5)
        
        # Overjet
        self.overjet_var = tk.IntVar(value=0)
        ttk.Label(self.inter_arch_frame, text="Overjet (mm):").grid(row=1, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.inter_arch_frame, from_=0, to=20, textvariable=self.overjet_var, width=5).grid(row=1, column=1)
        ttk.Label(self.inter_arch_frame, text="Weight: 3").grid(row=1, column=2, padx=5)
        
        # Overbite
        self.overbite_var = tk.IntVar(value=0)
        ttk.Label(self.inter_arch_frame, text="Overbite (mm):").grid(row=2, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.inter_arch_frame, from_=0, to=20, textvariable=self.overbite_var, width=5).grid(row=2, column=1)
        ttk.Label(self.inter_arch_frame, text="Weight: 2").grid(row=2, column=2, padx=5)
        
        # Crossbite
        self.crossbite_var = tk.IntVar(value=0)
        ttk.Label(self.inter_arch_frame, text="Crossbite (number of teeth):").grid(row=3, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.inter_arch_frame, from_=0, to=32, textvariable=self.crossbite_var, width=5).grid(row=3, column=1)
        ttk.Label(self.inter_arch_frame, text="Weight: 3").grid(row=3, column=2, padx=5)
        
        # Openbite
        self.openbite_var = tk.IntVar(value=0)
        ttk.Label(self.inter_arch_frame, text="Openbite (mm):").grid(row=4, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.inter_arch_frame, from_=0, to=20, textvariable=self.openbite_var, width=5).grid(row=4, column=1)
        ttk.Label(self.inter_arch_frame, text="Weight: 3").grid(row=4, column=2, padx=5)
        
        # Mesiodistal deviation
        self.mesiodistal_var = tk.IntVar(value=0)
        ttk.Label(self.inter_arch_frame, text="Mesiodistal deviation (mm):").grid(row=5, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.inter_arch_frame, from_=0, to=20, textvariable=self.mesiodistal_var, width=5).grid(row=5, column=1)
        ttk.Label(self.inter_arch_frame, text="Weight: 2").grid(row=5, column=2, padx=5)
        
    def create_deformities_section(self):
        # Dentofacial deformities
        ttk.Label(self.deformities_frame, text="Handicapping Dentofacial Deformities", font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=3, pady=5)
        
        # Facial and oral clefts
        self.clefts_var = tk.IntVar(value=0)
        ttk.Label(self.deformities_frame, text="Facial and oral clefts:").grid(row=1, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.deformities_frame, from_=0, to=3, textvariable=self.clefts_var, width=5).grid(row=1, column=1)
        ttk.Label(self.deformities_frame, text="Weight: 10").grid(row=1, column=2, padx=5)
        
        # Lower lip palatal to maxillary incisors
        self.lip_palatal_var = tk.IntVar(value=0)
        ttk.Label(self.deformities_frame, text="Lower lip palatal to maxillary incisors:").grid(row=2, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.deformities_frame, from_=0, to=1, textvariable=self.lip_palatal_var, width=5).grid(row=2, column=1)
        ttk.Label(self.deformities_frame, text="Weight: 8").grid(row=2, column=2, padx=5)
        
        # Occlusal interference
        self.occlusal_interference_var = tk.IntVar(value=0)
        ttk.Label(self.deformities_frame, text="Occlusal interference:").grid(row=3, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.deformities_frame, from_=0, to=3, textvariable=self.occlusal_interference_var, width=5).grid(row=3, column=1)
        ttk.Label(self.deformities_frame, text="Weight: 5").grid(row=3, column=2, padx=5)
        
        # Functional jaw limitation
        self.jaw_limitation_var = tk.IntVar(value=0)
        ttk.Label(self.deformities_frame, text="Functional jaw limitation:").grid(row=4, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.deformities_frame, from_=0, to=3, textvariable=self.jaw_limitation_var, width=5).grid(row=4, column=1)
        ttk.Label(self.deformities_frame, text="Weight: 5").grid(row=4, column=2, padx=5)
        
        # Facial asymmetry
        self.facial_asymmetry_var = tk.IntVar(value=0)
        ttk.Label(self.deformities_frame, text="Facial asymmetry:").grid(row=5, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.deformities_frame, from_=0, to=3, textvariable=self.facial_asymmetry_var, width=5).grid(row=5, column=1)
        ttk.Label(self.deformities_frame, text="Weight: 5").grid(row=5, column=2, padx=5)
        
        # Speech impairment
        self.speech_impairment_var = tk.IntVar(value=0)
        ttk.Label(self.deformities_frame, text="Speech impairment:").grid(row=6, column=0, sticky='w', padx=5)
        ttk.Spinbox(self.deformities_frame, from_=0, to=3, textvariable=self.speech_impairment_var, width=5).grid(row=6, column=1)
        ttk.Label(self.deformities_frame, text="Weight: 5").grid(row=6, column=2, padx=5)
        
    def create_results_section(self):
        # Results section
        ttk.Label(self.results_frame, text="HMAR Score Results", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Score display
        self.score_frame = ttk.LabelFrame(self.results_frame, text="Scores")
        self.score_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(self.score_frame, text="Intra-arch deviations score:").grid(row=0, column=0, sticky='w', padx=5, pady=2)
        self.intra_arch_label = ttk.Label(self.score_frame, text="0", font=('Arial', 10, 'bold'))
        self.intra_arch_label.grid(row=0, column=1, sticky='e', padx=5)
        
        ttk.Label(self.score_frame, text="Inter-arch deviations score:").grid(row=1, column=0, sticky='w', padx=5, pady=2)
        self.inter_arch_label = ttk.Label(self.score_frame, text="0", font=('Arial', 10, 'bold'))
        self.inter_arch_label.grid(row=1, column=1, sticky='e', padx=5)
        
        ttk.Label(self.score_frame, text="Dentofacial deformities score:").grid(row=2, column=0, sticky='w', padx=5, pady=2)
        self.deformities_label = ttk.Label(self.score_frame, text="0", font=('Arial', 10, 'bold'))
        self.deformities_label.grid(row=2, column=1, sticky='e', padx=5)
        
        ttk.Label(self.score_frame, text="TOTAL HMAR SCORE:", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.total_label = ttk.Label(self.score_frame, text="0", font=('Arial', 12, 'bold'))
        self.total_label.grid(row=3, column=1, sticky='e', padx=5)
        
        # Interpretation
        self.interpretation_frame = ttk.LabelFrame(self.results_frame, text="Interpretation")
        self.interpretation_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.interpretation_text = tk.Text(self.interpretation_frame, height=10, wrap='word')
        self.interpretation_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Add some initial text
        self.interpretation_text.insert('1.0', "Calculate the score to see the interpretation of the HMAR assessment.")
        self.interpretation_text.config(state='disabled')
        
    def calculate_score(self):
        try:
            # Calculate intra-arch deviations score
            missing_teeth = self.missing_teeth_var.get() * 3  # Weight: 3
            crowding = self.crowding_var.get() * 2            # Weight: 2
            rotation = self.rotation_var.get() * 1             # Weight: 1
            spacing = self.spacing_var.get() * 1               # Weight: 1
            self.intra_arch_score = missing_teeth + crowding + rotation + spacing
            
            # Calculate inter-arch deviations score
            overjet = self.overjet_var.get() * 3               # Weight: 3
            overbite = self.overbite_var.get() * 2             # Weight: 2
            crossbite = self.crossbite_var.get() * 3            # Weight: 3
            openbite = self.openbite_var.get() * 3              # Weight: 3
            mesiodistal = self.mesiodistal_var.get() * 2        # Weight: 2
            self.inter_arch_score = overjet + overbite + crossbite + openbite + mesiodistal
            
            # Calculate dentofacial deformities score
            clefts = self.clefts_var.get() * 10                 # Weight: 10
            lip_palatal = self.lip_palatal_var.get() * 8         # Weight: 8
            occlusal_interference = self.occlusal_interference_var.get() * 5  # Weight: 5
            jaw_limitation = self.jaw_limitation_var.get() * 5   # Weight: 5
            facial_asymmetry = self.facial_asymmetry_var.get() * 5  # Weight: 5
            speech_impairment = self.speech_impairment_var.get() * 5  # Weight: 5
            self.deformities_score = clefts + lip_palatal + occlusal_interference + jaw_limitation + facial_asymmetry + speech_impairment
            
            # Calculate total score
            self.total_score = self.intra_arch_score + self.inter_arch_score + self.deformities_score
            
            # Update the display
            self.intra_arch_label.config(text=str(self.intra_arch_score))
            self.inter_arch_label.config(text=str(self.inter_arch_score))
            self.deformities_label.config(text=str(self.deformities_score))
            self.total_label.config(text=str(self.total_score))
            
            # Update interpretation
            self.update_interpretation()
            
        except Exception as e:
            messagebox.showerror("Calculation Error", f"An error occurred during calculation: {str(e)}")
    
    def update_interpretation(self):
        self.interpretation_text.config(state='normal')
        self.interpretation_text.delete('1.0', 'end')
        
        interpretation = ""
        
        # Score ranges and interpretations
        if self.total_score == 0:
            interpretation = "Ideal occlusion. No significant malocclusion detected."
        elif 1 <= self.total_score <= 10:
            interpretation = "Mild malocclusion. Treatment may be considered for aesthetic reasons but is not essential for oral health."
        elif 11 <= self.total_score <= 25:
            interpretation = "Moderate malocclusion. Treatment is recommended to prevent potential oral health issues and improve function/aesthetics."
        elif 26 <= self.total_score <= 40:
            interpretation = "Severe malocclusion. Treatment is strongly recommended due to significant impact on oral health and function."
        else:
            interpretation = "Extremely severe malocclusion. Immediate treatment is essential due to serious functional and health implications."
        
        # Add detailed interpretation based on subscores
        interpretation += "\n\nDetailed Analysis:\n"
        
        if self.intra_arch_score > 15:
            interpretation += "- Significant intra-arch deviations present (missing teeth, crowding, etc.)\n"
        elif self.intra_arch_score > 5:
            interpretation += "- Noticeable intra-arch deviations present\n"
        else:
            interpretation += "- Minimal intra-arch deviations\n"
            
        if self.inter_arch_score > 15:
            interpretation += "- Severe inter-arch relationship problems (overjet, crossbite, etc.)\n"
        elif self.inter_arch_score > 5:
            interpretation += "- Moderate inter-arch relationship problems\n"
        else:
            interpretation += "- Minimal inter-arch relationship problems\n"
            
        if self.deformities_score > 15:
            interpretation += "- Significant dentofacial deformities present (clefts, asymmetry, etc.)\n"
        elif self.deformities_score > 5:
            interpretation += "- Some dentofacial deformities present\n"
        else:
            interpretation += "- Minimal or no dentofacial deformities\n"
        
        # Add general recommendations
        interpretation += "\nRecommendations:\n"
        if self.total_score >= 26:
            interpretation += "- Urgent orthodontic consultation recommended\n- Comprehensive treatment plan needed\n- Possible interdisciplinary approach required"
        elif self.total_score >= 11:
            interpretation += "- Orthodontic consultation recommended\n- Treatment likely beneficial\n- Monitor progression"
        else:
            interpretation += "- Routine dental monitoring sufficient\n- Treatment optional based on patient concerns"
        
        self.interpretation_text.insert('1.0', interpretation)
        self.interpretation_text.config(state='disabled')
    
    def reset_form(self):
        # Reset all variables to 0
        self.missing_teeth_var.set(0)
        self.crowding_var.set(0)
        self.rotation_var.set(0)
        self.spacing_var.set(0)
        
        self.overjet_var.set(0)
        self.overbite_var.set(0)
        self.crossbite_var.set(0)
        self.openbite_var.set(0)
        self.mesiodistal_var.set(0)
        
        self.clefts_var.set(0)
        self.lip_palatal_var.set(0)
        self.occlusal_interference_var.set(0)
        self.jaw_limitation_var.set(0)
        self.facial_asymmetry_var.set(0)
        self.speech_impairment_var.set(0)
        
        # Reset scores
        self.intra_arch_score = 0
        self.inter_arch_score = 0
        self.deformities_score = 0
        self.total_score = 0
        
        # Update display
        self.intra_arch_label.config(text="0")
        self.inter_arch_label.config(text="0")
        self.deformities_label.config(text="0")
        self.total_label.config(text="0")
        
        # Reset interpretation
        self.interpretation_text.config(state='normal')
        self.interpretation_text.delete('1.0', 'end')
        self.interpretation_text.insert('1.0', "Calculate the score to see the interpretation of the HMAR assessment.")
        self.interpretation_text.config(state='disabled')
    
    def show_ideal_values(self):
        ideal_values = """
        Ideal Values for Reference:
        
        Intra-arch Deviations:
        - Missing teeth: 0
        - Crowding: 0 mm per arch
        - Rotation: 0 degrees per tooth
        - Spacing: 0 mm per arch
        
        Inter-arch Deviations:
        - Overjet: 2-3 mm
        - Overbite: 2-3 mm
        - Crossbite: 0 teeth
        - Openbite: 0 mm
        - Mesiodistal deviation: 0 mm
        
        Dentofacial Deformities:
        - All should be 0 (none present)
        """
        messagebox.showinfo("Ideal Values", ideal_values)

if __name__ == "__main__":
    root = tk.Tk()
    app = HMARApp(root)
    root.mainloop()