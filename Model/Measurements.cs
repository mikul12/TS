using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace measurements_end.Model
{
    [Table("measurements")]
    public partial class Measurements
    {
        [Key]
        [Column("id")]
        public int Id { get; set; }
        [Column("camId", TypeName = "text")]
        public string CamId { get; set; }
        [Column("carsDetected")]
        public double? CarsDetected { get; set; }
        [Column("datetime", TypeName = "datetime")]
        public DateTime? Datetime { get; set; }
        [Column("crowd")]
        public double? Crowd { get; set; }
    }
}
