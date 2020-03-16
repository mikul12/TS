using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace measurements_last2.Model
{
    [Table("measurements")]
    public partial class Measurements
    {
        [Key]
        [Column("camId")]
        [StringLength(30)]
        public string CamId { get; set; }
        [Column("carsDetected")]
        public int? CarsDetected { get; set; }
        [Column("dateTime", TypeName = "date")]
        public DateTime? DateTime { get; set; }
    }
}
