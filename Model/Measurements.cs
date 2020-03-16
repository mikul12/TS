using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace measurements_lastlast.Model
{
    [Table("measurements")]
    public partial class Measurements
    {
        [Key]
        [Column("id")]
        public int Id { get; set; }
        [Column("camId")]
        [StringLength(40)]
        public string CamId { get; set; }
        [Column("carsDetected")]
        [StringLength(50)]
        public double? CarsDetected { get; set; }
        [Column("dateTime", TypeName = "datetime")]
        public DateTime? DateTime { get; set; }
        [Column("crowd")]
        public double? Crowd { get; set; }
    }
}
