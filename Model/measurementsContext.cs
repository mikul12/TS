using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;

namespace measurements_last2.Model
{
    public partial class measurementsContext : DbContext
    {
        public measurementsContext()
        {
        }

        public measurementsContext(DbContextOptions<measurementsContext> options)
            : base(options)
        {
        }

        public virtual DbSet<Measurements> Measurements { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. See http://go.microsoft.com/fwlink/?LinkId=723263 for guidance on storing connection strings.
                optionsBuilder.UseSqlServer("Server=tcp:traffic2.database.windows.net,1433;Initial Catalog=measurements;Persist Security Info=False;User ID=admin2;Password=admin4321@;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;");
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Measurements>(entity =>
            {
                entity.HasKey(e => e.CamId)
                    .HasName("PK__measurem__16DA075209FF603B");

                entity.Property(e => e.CamId).IsUnicode(false);
            });

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
